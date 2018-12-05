# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MM_createcode_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateCode(object):
    def setupUi(self, CreateCode):
        CreateCode.setObjectName("CreateCode")
        CreateCode.resize(400, 300)
        CreateCode.setMinimumSize(QtCore.QSize(0, 50))
        self.widget = QtWidgets.QWidget(CreateCode)
        self.widget.setGeometry(QtCore.QRect(0, 30, 402, 229))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.code_row = QtWidgets.QTableWidget(self.widget)
        self.code_row.setMinimumSize(QtCore.QSize(100, 0))
        self.code_row.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.code_row.setFont(font)
        self.code_row.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.code_row.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.code_row.setRowCount(1)
        self.code_row.setColumnCount(5)
        self.code_row.setObjectName("code_row")
        self.code_row.horizontalHeader().setVisible(False)
        self.code_row.horizontalHeader().setCascadingSectionResizes(True)
        self.code_row.horizontalHeader().setDefaultSectionSize(77)
        self.code_row.horizontalHeader().setMinimumSectionSize(70)
        self.code_row.verticalHeader().setVisible(False)
        self.code_row.verticalHeader().setCascadingSectionResizes(True)
        self.code_row.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.code_row)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.submit_b = QtWidgets.QPushButton(self.widget)
        self.submit_b.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.submit_b.setFont(font)
        self.submit_b.setObjectName("submit_b")
        self.verticalLayout.addWidget(self.submit_b)

        self.retranslateUi(CreateCode)
        QtCore.QMetaObject.connectSlotsByName(CreateCode)

    def retranslateUi(self, CreateCode):
        _translate = QtCore.QCoreApplication.translate
        CreateCode.setWindowTitle(_translate("CreateCode", "Create Code"))
        self.submit_b.setText(_translate("CreateCode", "Submit"))

