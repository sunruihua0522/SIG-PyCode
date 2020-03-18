from PyQt5.QtWidgets import QGridLayout,QHBoxLayout,QLineEdit, QApplication,QMainWindow,QWidget,QLabel,QPushButton
from PyQt5 import QtCore,QtGui
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()


        self.InitWindow()

        self.show()
    def InitWindow(self):
        rootWidget = QWidget(self)
        self.setCentralWidget(rootWidget)
        self.setGeometry(100,200,800,600)

        hbox = QHBoxLayout()

        label = QLabel("name")
        label.setFont(QtGui.QFont('JetBrains Mono',20))

        lineedit = QLineEdit()
        lineedit.setPlaceholderText('Please enter your register code')
        lineedit.setFont(QtGui.QFont('JetBrains Mono',20))

        btn = QPushButton('Sumbit')
        btn.setFont(QtGui.QFont('JetBrains Mono',20))

        hbox.addWidget(label)
        hbox.addStretch(1)
        hbox.addWidget(lineedit)
        hbox.addStretch(2)
        hbox.addWidget(btn)
        hbox.addStretch(5)


        rootWidget.setLayout(hbox)



if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MyWindow()

    sys.exit(App.exec())