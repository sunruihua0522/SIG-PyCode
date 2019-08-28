from untitled import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
class MyGui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyGui,self).__init__(parent)
        self.setupUi(self)

if __name__=='__main__':
    App=QApplication(sys.argv)
    ui=MyGui()
    ui.show()
    sys.exit(App.exec_())