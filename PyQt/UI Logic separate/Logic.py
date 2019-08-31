from gui import Ui_MainWindow
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication

class MyGui(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super(MyGui,self).__init__(None) #需要给QMainWindow初始化构造函数
        self.setupUi(self)
        #self.__Binding()

    def __Binding(self):
        self.pushButton.clicked.connect(self.__onButtonClicked)

    def __onButtonClicked(self):
        self.textEdit.setText(self.textEdit_2.toPlainText())

    @pyqtSlot(bool)
    def on_pushButton_clicked(self,clicked):
        self.textEdit.setText(self.textEdit_2.toPlainText())

if __name__=='__main__':
    App = QApplication(sys.argv)
    Gui = MyGui()
    Gui.show()
    sys.exit(App.exec_())


exit()