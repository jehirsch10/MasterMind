# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MM_endgame_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EndGame(object):
    def setupUi(self, EndGame):
        EndGame.setObjectName("EndGame")
        EndGame.resize(400, 409)
        self.layoutWidget = QtWidgets.QWidget(EndGame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 378, 393))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textEdit.setBaseSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.play_b = QtWidgets.QPushButton(self.layoutWidget)
        self.play_b.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.play_b.setFont(font)
        self.play_b.setObjectName("play_b")
        self.verticalLayout.addWidget(self.play_b)
        self.exit_b = QtWidgets.QPushButton(self.layoutWidget)
        self.exit_b.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.exit_b.setFont(font)
        self.exit_b.setObjectName("exit_b")
        self.verticalLayout.addWidget(self.exit_b)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_2.setMaximumSize(QtCore.QSize(16777215, 130))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout.addWidget(self.textEdit_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(EndGame)
        QtCore.QMetaObject.connectSlotsByName(EndGame)

    def retranslateUi(self, EndGame):
        _translate = QtCore.QCoreApplication.translate
        EndGame.setWindowTitle(_translate("EndGame", "End Game"))
        self.textEdit.setHtml(_translate("EndGame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">MasterMind</span></p></body></html>"))
        self.play_b.setText(_translate("EndGame", "Play Again"))
        self.exit_b.setText(_translate("EndGame", "Exit"))

