import sys
sys.path.append('../')
from SigContact import SigContact
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QPushButton,\
    QTextEdit,QLineEdit,QGridLayout,QVBoxLayout,QHBoxLayout
from PyQt5 import QtGui,QtCore


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initGui()
        self.show()

    def initGui(self):
        # init window
        self.setWindowTitle("Look up contact")
        self.setGeometry(100,200,800,600)

        left = QWidget()
        left.setStyleSheet("background-color:black")


        top = QLabel('Look up system')
        top.setStyleSheet("background-color:#C8C8C8C8;font-size:30px")


        bottom = QWidget()


        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        gridBox = QGridLayout()

        gridBox.addWidget(left,0,0,4,1)
        gridBox.addWidget(top,0,1,1,4)
        gridBox.addWidget(bottom,1,1,3,4)
        gridBox.setSpacing(0)


        # Left control
        buttonLookup = QPushButton('Check')
        buttonLookup.clicked.connect(self.onCheckOutclick)
        buttonLookup.setStyleSheet("color:white;background-color:#C8C8C8C8;font-size:25px")
        vbox.addWidget(buttonLookup)
        vbox.addStretch()
        left.setLayout(vbox)

        self.setLayout(gridBox)

    def onCheckOutclick(self):
        engine = create_engine("mysql+pymysql://root:sMx141110~@localhost:3306/testforwindows", encoding='utf-8',
                               echo=False)
        base = SigContact()
        base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()

        # user = session.query(SigContact).filter(SigContact.id == '5').one()
        user = session.query(SigContact).filter(SigContact.firstName.like('%ruihua%')).one()
        print(user.mobile, user.email, user.businessPhone)

        session.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
