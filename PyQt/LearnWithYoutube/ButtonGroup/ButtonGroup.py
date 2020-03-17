from PyQt5.QtWidgets import QButtonGroup, QVBoxLayout, QPushButton,QLabel,QWidget,QApplication
from PyQt5 import QtCore,QtGui
import sys
class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.icon = QtGui.QIcon("home.ico")
        self.rect = QtCore.QRect(100,200,800,600)
        self.title = "PyQt5 BuggonGroup"

        self.setWindowIcon(self.icon)
        self.setWindowTitle(self.title)
        self.setGeometry(self.rect)
        self.label = QLabel(self)
        self.label.setText('label')
        self.button_group = QButtonGroup()
        self.InitWindow()
        self.show()

    def InitWindow(self):
        '''
        QButtonGroup的signal再使用的时候要注意如何使用[int]不要忘记了,否则会出错
        :return:
        '''
        self.button_group.buttonClicked[int].connect(self.OnButtonGroupPressed)
        vbox = QVBoxLayout()
        for i in range(1,10):
            button = QPushButton('Button %d'%i)
            button.setIcon(self.icon)
            button.setIconSize(QtCore.QSize(40,40))
            button.setFont(QtGui.QFont('lisu',20))
            self.button_group.addButton(button,i)
            vbox.addWidget(button)



        self.label.setFont(QtGui.QFont('lisu',20))
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def OnButtonGroupPressed(self,id):
        self.label.setText(self.button_group.button(id).text())

if __name__ == "__main__":
    App = QApplication(sys.argv)

    window = MyWindow()

    sys.exit(App.exec())
