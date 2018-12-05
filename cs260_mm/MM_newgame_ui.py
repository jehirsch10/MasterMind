# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MM_newgame_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewGame(object):
    def setupUi(self, NewGame):
        NewGame.setObjectName("NewGame")
        NewGame.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(NewGame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.breaker_b = QtWidgets.QPushButton(NewGame)
        self.breaker_b.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.breaker_b.setFont(font)
        self.breaker_b.setObjectName("breaker_b")
        self.verticalLayout.addWidget(self.breaker_b)
        self.maker_b = QtWidgets.QPushButton(NewGame)
        self.maker_b.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.maker_b.setFont(font)
        self.maker_b.setObjectName("maker_b")
        self.verticalLayout.addWidget(self.maker_b)
        self.gridLayout.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(NewGame)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.retranslateUi(NewGame)
        QtCore.QMetaObject.connectSlotsByName(NewGame)

    def retranslateUi(self, NewGame):
        _translate = QtCore.QCoreApplication.translate
        NewGame.setWindowTitle(_translate("NewGame", "New Game"))
        self.breaker_b.setText(_translate("NewGame", "PLAY AS CODEBREAKER"))
        self.maker_b.setText(_translate("NewGame", "PLAY AS CODEMAKER"))
        self.textEdit.setHtml(_translate("NewGame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">MasterMind</span></p></body></html>"))

