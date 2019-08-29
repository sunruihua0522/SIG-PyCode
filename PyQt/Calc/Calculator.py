# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 216)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit_Num2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Num2.setGeometry(QtCore.QRect(200, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_Num2.setFont(font)
        self.textEdit_Num2.setObjectName("textEdit_Num2")
        self.textEdit_Num1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Num1.setGeometry(QtCore.QRect(10, 50, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_Num1.setFont(font)
        self.textEdit_Num1.setObjectName("textEdit_Num1")
        self.comboBox_symbol = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_symbol.setGeometry(QtCore.QRect(120, 60, 69, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_symbol.setFont(font)
        self.comboBox_symbol.setObjectName("comboBox_symbol")
        self.comboBox_symbol.addItem("")
        self.comboBox_symbol.addItem("")
        self.comboBox_symbol.addItem("")
        self.comboBox_symbol.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 70, 21, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit_Result = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Result.setGeometry(QtCore.QRect(340, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_Result.setFont(font)
        self.textEdit_Result.setObjectName("textEdit_Result")
        self.pushButton_calc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc.setGeometry(QtCore.QRect(370, 130, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_calc.setFont(font)
        self.pushButton_calc.setObjectName("pushButton_calc")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_symbol.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox_symbol.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox_symbol.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox_symbol.setItemText(2, _translate("MainWindow", "*"))
        self.comboBox_symbol.setItemText(3, _translate("MainWindow", "/"))
        self.label.setText(_translate("MainWindow", "="))
        self.pushButton_calc.setText(_translate("MainWindow", "Calc"))
