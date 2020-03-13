from Calculator import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMessageBox

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
class MyGui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent):
        super(MyGui,self).__init__(parent)
        self.setupUi(self)
        self.pushButton_calc.pressed.connect(self.OnPress)

    def Calc(self, a,b,sy):
        if sy=='+':
            return a+b
        elif sy=='-':
            return a-b
        elif sy=='*':
            return a*b
        else:
            return a/b
    def OnPress(self):
        self.textEdit_Result.setText(str(self.Calc(int(self.textEdit_Num1.toPlainText()),int(self.textEdit_Num2.toPlainText()),self.comboBox_symbol.currentText())))

if __name__=='__main__':
    App=QApplication(sys.argv)
    ui=MyGui()
    ui.show()
    sys.exit(App.exec_())