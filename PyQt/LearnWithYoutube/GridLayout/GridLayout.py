from PyQt5.QtWidgets import QGridLayout, QApplication,QMainWindow,QWidget,QLabel,QPushButton
from PyQt5 import QtCore,QtGui
import sys
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GridLayout')
        self.InitCtrl()

        self.show()


    def InitCtrl(self):
        gridLayout = QGridLayout(self)

        for i in range(1,5):
            for j in range(1,10):

                label = QLabel('%drow%dcol'%(i,j))
                if i%2 == 0:
                    label.setStyleSheet("color:red;")
                if j%2 == 0:
                    label.setStyleSheet("color:green;")
                label.setFont(QtGui.QFont('JetBrains Mono',20))
                gridLayout.addWidget(label,i-1,j-1)
        gridLayout.setMenuBar(QPushButton('Munu push button'))
        gridLayout.setSpacing(25)

        widget = QWidget(self)
        self.setCentralWidget(widget)
        widget.setLayout(gridLayout)

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MyWindow()

    sys.exit(App.exec())