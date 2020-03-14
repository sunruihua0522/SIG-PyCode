from PyQt5.QtWidgets import QApplication,QHBoxLayout,QVBoxLayout
from PyQt5.QtWidgets import  QDialog, QGroupBox,QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QSize
from PyQt5 import QtCore

class MyDialog(QDialog):
    def __init__(self):
        super(MyDialog, self).__init__()

        self.title = 'PyQt5 Layout WIndows'
        self.rect = QRect(500,200,800,600)
        self.icon = QtGui.QIcon('home.ico')

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.rect)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What's your favote sport")
        hboxLayout = QHBoxLayout()


        button1 = QPushButton('Football',self)
        #button1.setGeometry(QRect(100,100,150,40))
        button1.setIconSize(QSize(30,30))
        button1.setIcon(self.icon)

        button2 = QPushButton('Basketball', self)
        #button2.setGeometry(QRect(100, 100, 150, 40))
        button2.setIconSize(QSize(30, 30))
        button2.setIcon(self.icon)

        #Add button to HBoxLayout
        hboxLayout.addWidget(button1)
        hboxLayout.addWidget(button2)

        self.groupBox.setLayout(hboxLayout)

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MyDialog()
    sys.exit(App.exec())