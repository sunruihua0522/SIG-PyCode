from PyQt5.QtWidgets import QGridLayout, QGroupBox,QCheckBox,\
    QApplication,QDialog,QVBoxLayout, QLabel,QMessageBox
from PyQt5 import QtGui, QtCore
import sys

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.icon = QtGui.QIcon("home.ico")
        self.title = "Gridbox and Checkbox"
        self.rect = QtCore.QRect(100,200,800,600)
        self.label = QLabel('Text')
        self.initWindow()
        self.SetCheckbox()

    def initWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(self.icon)
        self.setGeometry(self.rect)
        self.show()


    def SetCheckbox(self):
        captionList = ['Basketball','fottball','jump','run','Go','Java']
        groupBox = QGroupBox("What's your favorate sports")
        groupBox.setFont(QtGui.QFont('JetBrains Mono',20))
        gridLayout = QGridLayout()
        for i in range(0,3):
            for j in range(0,2):
                checkbox = QCheckBox(captionList[2*i+j])
                checkbox.setIcon(self.icon)
                checkbox.setIconSize(QtCore.QSize(40,40))
                checkbox.setFont(QtGui.QFont("JetBrains Mono",15))
                checkbox.setStyleSheet("color:red;")
                checkbox.toggled.connect(self.OnToggled)
                gridLayout.addWidget(checkbox,i,j)
        groupBox.setLayout(gridLayout)
        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(groupBox)
        vboxlayout.addWidget(self.label)
        self.setLayout(vboxlayout)

    def OnToggled(self,isToggled):
        self.label.setText(str(isToggled))

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())