'''
@author: Jeremy Hirsch
'''

'''
Color codes: 0 - white, 1 - yellow, 2 - green, 3 - red, 4 - blue, 5 - black
'''

'''
Codes are represented as lists of length 4 of integers ranging from 0 to 5
Score is not associated with code but with the row
Row is an object which includes among its attributes a code and its score, along with the GUI representation of the code 
'''

#imports
import sys
import os
import os.path
import random
import time
import sqlite3
from PyQt5 import QtCore, QtGui 
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QPushButton, QInputDialog, QDialog, QSizePolicy, QHeaderView, QVBoxLayout, QFileDialog
from cs260_mm.MM_mainwin_ui import Ui_MainWindow
from cs260_mm.MM_endgame_ui import Ui_EndGame
from cs260_mm.MM_newgame_ui import Ui_NewGame
from cs260_mm.MM_createcode_ui import Ui_CreateCode
from PyQt5.QtGui import QCloseEvent


class MM_Main_Win(QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None): # DONE
        super(MM_Main_Win, self).__init__()
        self.setupUi(self)
        
        # some vars
        self.current_row = 0
        self.type = "Not yet assigned"
        
        # title bar buttons
        flags = Qt.WindowFlags(Qt.WindowMinimizeButtonHint| Qt.WindowMaximizeButtonHint| Qt.WindowCloseButtonHint)
        self.setWindowFlags(flags)
        
        # buttons
        self.newgame_b.clicked.connect(self.new_game)
        self.submit_b.clicked.connect(self.submit_code)
        self.next_b.clicked.connect(self.break_code)
        
        # containers
        self.rows = []
        self.guesses = [] 
        
        # black peg, white peg
        self.possible_scores = [[0,0],[0,1],[0,2],[0,3],[0,4],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[3,0],[4,0]]
        
        # start game
        self.new_game() # sets type of game
        if self.type == "Not yet assigned":
            quit()  
    
    def new_game(self): # DONE set type of game
        # open new game dialog
        new_NewGameDialog = NewGameDialog()
        new_NewGameDialog.exec_()
    
        # return new game type
        if not new_NewGameDialog.type == "Not yet assigned":
            self.type = new_NewGameDialog.type
            self.gametype.setText(f"MasterMind: {self.type}") # GUI label for type of game
        
            # set up secret code
            self.current_row = 0
            self.create_code()
            
            # get game going
            self.guesstable.clear()
            self.guesstable.setRowCount(0)
            self.rows = []
            self.guesses = []
            self.unused_set = []
            self.sol_set = []
            self.init_guess = [0,0,1,1]
            self.create_row()
            if self.type is "codemaker":
                self.submit_b.setEnabled(False)
                self.next_b.setEnabled(True)
                self.break_code(first = True)
                self.secrettable.setEnabled(True)
            else:
                self.submit_b.setEnabled(True)
                self.next_b.setEnabled(False)
                self.secrettable.setEnabled(False)

    
    def create_code(self): # DONE get/create secret code
        if self.type == "codemaker":
            # open create code dialog & get secret code
            new_CreateCodeDialog = CreateCodeDialog()
            new_CreateCodeDialog.exec_()
            self.secret_code = new_CreateCodeDialog.secret_code
            self.secrettable.insertRow(0)
            secret_row = MyRow(self.secrettable, 0, "N/a", False, True)
            for x in range(4):
                for y in range(self.secret_code[x]):
                    secret_row.change_color(secret_row.table.item(0,x+1))
        else:
            #generate random secret code
            self.secret_code = [random.randint(0,5) for _ in range(4)]
    
    def create_row(self): # DONE create a row on which to input a guess
        self.guesstable.insertRow(self.current_row)
        row = MyRow(self.guesstable, self.current_row, self.secret_code, False)
        self.rows.append(row)
    
    def submit_code(self): # DONE 
        self.rows[self.current_row].submit()
        if self.gametype == "codemaker":
            self.unused_set.remove(self.rows[self.current_row].code)
        if self.rows[self.current_row].correct_guess:
            if self.type == "codebreaker":
                self.game_over(f"You broke the code in {self.current_row + 1} guesses! <br>",self.secret_code)
            else:
                self.game_over(f"The bot broke your code in {self.current_row + 1} guesses! <br>", self.secret_code)
        else:
            self.current_row+=1
            self.create_row()

    def break_code(self, first = False): # DO THE NOTE *note: when creating rows make sure to not allow them to be color changed by user
        row = self.rows[self.current_row]
        if first:
            self.create_sol_set()           
            for x in range(4):
                for y in range(self.init_guess[x]):
                    row.change_color(row.table.item(self.current_row,x+1))
        else:
            # step 5 - remove from sol set any code that would not give the sames score if it was the secret code
            last_row = self.rows[self.current_row-1]
            self.sol_set = [x for x in self.sol_set if self.give_same_score(last_row.code,x,last_row.score_num)]
            # step 6
            if len(self.sol_set) == 1:
                self.next_guess = self.sol_set[0]
            else:
                self.next_guess = self.minimax()
            for x in range(4):
                for y in range(self.next_guess[x]):
                    row.change_color(row.table.item(self.current_row,x+1))
        self.submit_code()
        
    def create_sol_set(self): # DONE creates list of possible codes
        for p in range(6):
            for q in range(6):
                for r in range(6):
                    for s in range(6):
                        self.sol_set.append([p,q,r,s])
                        self.unused_set.append([p,q,r,s])
    
    def give_same_score(self, guess, sol, score): # DONE shitty name
        this_score = self.check_score(guess, sol)
        return this_score == score
    
    def check_score(self, guess, sol): # DONE
        score = []
        black = 0 # count of black pegs(code elements in right spot)
        white = 0 # count of white pegs(code elements in wrong spot)
        temp_guess = guess[:]
        temp_sol = sol[:]
        for x in range(4):
            if temp_guess[x] == temp_sol[x]:
                black += 1
                temp_guess[x] = -1
                temp_sol[x] = -2
        for x in temp_guess:
            if x in temp_sol:
                white += 1
                temp_sol[temp_sol.index(x)] = -2   
        score.append(black)
        score.append(white)
        return score
    
    def minimax(self): # DONE?
        highest_score = 0
        high_scorers = []
        for code in self.unused_set:
            hits_per_peg_score = {f"{x}".replace(" ", "") : 0 for x in self.possible_scores}
            for sol in self.sol_set:
                hits_per_peg_score[f"{self.check_score(code, sol)}".replace(" ","")] += 1 
            score = len(self.sol_set) - max(hits_per_peg_score.values())
            if score > highest_score:
                highest_score = score
                high_scorers = [code]
            elif score == highest_score:
                high_scorers.append(code)
        for guess in high_scorers:
            if guess in self.sol_set:
                return guess
        return high_scorers[0]
          
    def help(self): # todo(not important)
        # spawn a help qdialog that I havent made yet
        pass
    
    def game_over(self, msg, secret): # DONE
        # open end game dialog
        new_EndGameDialog = EndGameDialog(msg, secret)
        new_EndGameDialog.exec_()
        # start new game
        self.type == "Not yet assigned"
        self.new_game()
    
    def closeEvent(self, event, msg = True): # DONE confirm close dialog
        if msg == True:
            reply = QMessageBox.question(self, 'Message',"Are you sure you want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()    
        else:
            event.accept


class MyRow(QObject): # DONE row
#     needs_callback = pyqtSignal()
#     stat_sum = pyqtSignal('PyQt_PyObject')
#     update_sig = pyqtSignal()
#     conn_sig = pyqtSignal(int)
    
    def __init__(self, table, current_row, secret, codemaker, input_secret = False): # DONE
        super().__init__()
        
        # get/create var.s
        self.table = table
        self.current_row = current_row
        self.score_text = ""
        self.score_num = []
        self.score_item = QTableWidgetItem()
        self.secret_code = secret
        self.submitted = False
        self.code = []
        self.correct_guess = False
        self.codemaker = codemaker
        
        # set up row items
        self.guess_num_item = QTableWidgetItem(f"Guess {self.current_row+1}")
        self.guess_code1_item = QTableWidgetItem("0")
        self.guess_code1_item.setBackground(QtGui.QColor(255,255,255))
        self.guess_code1_item.setForeground(QtGui.QColor(255,255,255))
        self.guess_code2_item = QTableWidgetItem("0")
        self.guess_code2_item.setBackground(QtGui.QColor(255,255,255))
        self.guess_code2_item.setForeground(QtGui.QColor(255,255,255))
        self.guess_code3_item = QTableWidgetItem("0")
        self.guess_code3_item.setBackground(QtGui.QColor(255,255,255))
        self.guess_code3_item.setForeground(QtGui.QColor(255,255,255))
        self.guess_code4_item = QTableWidgetItem("0")
        self.guess_code4_item.setBackground(QtGui.QColor(255,255,255))
        self.guess_code4_item.setForeground(QtGui.QColor(255,255,255))
        
        # connect items to color changer
        self.table.itemClicked.connect(self.change_color)

        # if creating secret code then first item shouldn't say guess number
        if input_secret:
            self.guess_num_item.setText("code:")
        
        # place items in row 
        self.table.setItem(self.current_row, 0, self.guess_num_item)
        self.table.setItem(self.current_row, 1, self.guess_code1_item)
        self.table.setItem(self.current_row, 2, self.guess_code2_item)
        self.table.setItem(self.current_row, 3, self.guess_code3_item)
        self.table.setItem(self.current_row, 4, self.guess_code4_item)
             
    def submit(self): # DONE
        self.submitted = True
        self.table.itemClicked.disconnect()
        self.get_code()
        self.score()     
    
    def score(self): # DONE (and tested elsewhere) *if score is 4 black dots change correct guess to true
        black = 0 # count of black pegs(code elements in right spot)
        white = 0 # count of white pegs(code elements in wrong spot)
        if self.code == self.secret_code:
            self.correct_guess = True
        else:
            temp_code = self.code[:]
            temp_secret = self.secret_code[:]
            for x in range(4):
                if temp_code[x] == temp_secret[x]:
                    black += 1
                    temp_code[x] = -1
                    temp_secret[x] = -2
            for x in temp_code:
                if x in temp_secret:
                    white += 1
                    temp_secret[temp_secret.index(x)] = -2
            for x in range(black):
                self.score_text += u'\u2022'
            for x in range(white):
                self.score_text += "o"   
        self.score_num.append(black)
        self.score_num.append(white)
        self.score_item.setText(self.score_text)
        self.table.setItem(self.current_row, 5, self.score_item)
                    
    def change_color(self, item): # DONE change color
        if (item is not self.guess_num_item) and (item is not self.score_item) and (item.row() == self.current_row) and not self.codemaker:
            num = item.text()
            if num == "0":
                item.setText("1")
                item.setBackground(QtGui.QColor(255,255,0))
                item.setForeground(QtGui.QColor(255,255,0))
            elif num == "1":
                item.setText("2")
                item.setBackground(QtGui.QColor(0,255,0))
                item.setForeground(QtGui.QColor(0,255,0))
            elif num == "2":
                item.setText("3")
                item.setBackground(QtGui.QColor(255,0,0))
                item.setForeground(QtGui.QColor(255,0,0))
            elif num == "3":
                item.setText("4")
                item.setBackground(QtGui.QColor(0,0,255))
                item.setForeground(QtGui.QColor(0,0,255))
            elif num == "4":
                item.setText("5")
                item.setBackground(QtGui.QColor(0,0,0))
                item.setForeground(QtGui.QColor(0,0,0))
            elif num == "5":
                item.setText("0")
                item.setBackground(QtGui.QColor(255,255,255))
                item.setForeground(QtGui.QColor(255,255,255))
         
    def get_code(self): # DONE get code of row
        for x in range(4):
            self.code.append(int(self.table.item(self.current_row,x+1).text()))
           
            
class CreateCodeDialog(QDialog, Ui_CreateCode): # DONE create secret code
    def __init__(self, parent = None): 
        super(CreateCodeDialog, self).__init__()
        self.setupUi(self)
         
        # title bar buttons
        flags = Qt.WindowFlags(Qt.WindowMinimizeButtonHint| Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(flags)
         
        # button
        self.submit_b.clicked.connect(self.submit)
         
        # secret code
        self.secret_code = []
        
        # create a row on which to input the secret code
        self.row = MyRow(self.code_row, 0, "N/a", False, input_secret= True)
        
    def submit(self): # DONE do upon clicking submit
        self.row.get_code()
        self.secret_code = self.row.code
        self.accept()


class NewGameDialog(QDialog, Ui_NewGame): # DONE start game of desired type
    def __init__(self, parent = None): 
        super(NewGameDialog, self).__init__()
        self.setupUi(self)
         
        # title bar buttons
        flags = Qt.WindowFlags(Qt.WindowMinimizeButtonHint| Qt.WindowMaximizeButtonHint| Qt.WindowCloseButtonHint)
        self.setWindowFlags(flags)
         
        # connect buttons
        self.maker_b.clicked.connect(self.maker)
        self.breaker_b.clicked.connect(self.breaker)
         
        # game type
        self.type = "Not yet assigned"
         
    def maker(self): # choose codemaker
        self.type = "codemaker"
        self.accept()
    
    def breaker(self): # choose codebreaker
        self.type = "codebreaker"
        self.accept()
                

class EndGameDialog(QDialog, Ui_EndGame): # DONE close or play again
    def __init__(self, msg, secret):
        super(EndGameDialog, self).__init__()
        self.setupUi(self)
         
        # title bar buttons
        flags = Qt.WindowFlags(Qt.WindowMinimizeButtonHint| Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(flags)
        # connect buttons
        self.play_b.clicked.connect(self.play)
        self.exit_b.clicked.connect(self.exit)
        # set up msg
        msg += "The secret code was: "
        for num in secret:
            if num == 0:
                msg += "white "
            elif num == 1:
                msg += "yellow "
            elif num == 2:
                msg += "green "
            elif num == 3:
                msg += "red "
            elif num == 4:
                msg += "blue "
            elif num == 5:
                msg += "black "
        self.textEdit_2.setText(msg)
         
    def play(self): # play again
        self.accept()
         
    def exit(self): # exit
        exit()
     
    def displayResult(self, my_str): # parse the string, return list of tuples
        pass


def main():
    my_app = QApplication(sys.argv)
    MM = MM_Main_Win()
    MM.show()
    sys.exit(my_app.exec_())
    
if __name__ == '__main__':
    main()