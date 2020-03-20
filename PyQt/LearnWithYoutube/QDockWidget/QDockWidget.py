from PyQt5.QtWidgets import QApplication, QMainWindow, QDockWidget,QWidget,\
    QVBoxLayout,QMenu,QAction,QMenuBar,QStatusBar,QLabel,QHBoxLayout,QTextEdit
from PyQt5 import QtGui,QtCore

import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.InitGui()
        self.show()

    def InitGui(self):
        self.setGeometry(100,200,800,600)
        self.setWindowTitle('QDockWidget')

        #Add Menu
        menuBar = QMenuBar()
        menu = menuBar.addMenu('Edit')
        menu.addAction('Copy')
        menu.addAction('Cut')
        menu.addAction('Paste')
        self.setMenuBar(menuBar)



        #Add status Bar
        statusBar = QStatusBar()
        statusBar.addWidget(QLabel("It's a status bar"))
        self.setStatusBar(statusBar)


        #Add Left dock widget
        left = QDockWidget('Left DockWidget')
        vbox = QVBoxLayout()
        for i in range(1,10):
            vbox.addWidget(QLabel('Left %d'%i))
        leftWidget = QWidget()
        leftWidget.setLayout(vbox)
        left.setWidget(leftWidget)
        leftWidget.setStyleSheet("background-color:lightblue;color:white;")
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea,left)

        # Add right dock widget
        Right = QDockWidget('Right DockWidget')
        vbox = QVBoxLayout()
        for i in range(1, 10):
            vbox.addWidget(QLabel('Right %d' % i))
        RightWidget = QWidget()
        RightWidget.setLayout(vbox)
        Right.setWidget(RightWidget)
        RightWidget.setStyleSheet("background-color:lightblue;color:white;")
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, Right)

        # Add top dock widget
        Top = QDockWidget('Top DockWidget')
        vbox = QVBoxLayout()
        for i in range(1, 5):
            vbox.addWidget(QLabel('Top %d' % i))
        TopWidget = QWidget()
        TopWidget.setLayout(vbox)
        Top.setWidget(TopWidget)
        TopWidget.setStyleSheet("background-color:lightblue;color:white;")
        self.addDockWidget(QtCore.Qt.TopDockWidgetArea, Top)

        # Add bottom dock widget
        Bottom = QDockWidget('Bottom DockWidget')
        vbox = QVBoxLayout()
        for i in range(1, 5):
            vbox.addWidget(QLabel('Bottom %d' % i))
        BottomWidget = QWidget()
        BottomWidget.setLayout(vbox)
        Bottom.setWidget(BottomWidget)
        BottomWidget.setStyleSheet("background-color:lightblue;color:white;")
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, Bottom)


        #Center
        self.rootWidget = QWidget()
        self.setCentralWidget(self.rootWidget)
        hbox = QHBoxLayout()
        hbox.addWidget(QTextEdit('Center'))
        self.rootWidget.setLayout(hbox)

        pass
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(App.exec())