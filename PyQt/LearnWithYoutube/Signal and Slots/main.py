from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QSize
from PyQt5 import QtCore

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = 'Signal and Slots'
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 300
        self.icon = 'home.ico'
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.UIComponents()
        self.show()

    def UIComponents(self):
        button = QPushButton('Click me', self)
        #button.move(50,50)
        button.setGeometry(QRect(100,100,100,40))
        button.setIcon(QtGui.QIcon(self.icon))
        button.setIconSize(QSize(25,25))
        button.setToolTip('<h3>This</h3> is push button')
        button.clicked.connect(self.ClickMe)
        button.clicked.connect(self.ShutDown)

    def ClickMe(self):
        print('Hello world')

    def ShutDown(self):
        exit()

if __name__ == '__main__':
    App =QApplication(sys.argv)
    window = Window()

    sys.exit(App.exec())
