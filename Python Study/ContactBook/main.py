import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

import xlrd
#dialect+driver://root:1q2w3e4r5t@127.0.0.1:3306/dbname?charset=UTF8MB4


class SigContact(declarative_base(())):
    __tablename__ = 'SigContact'
    id = Column(Integer,primary_key=True)
    firstName = Column(String(30))
    middleName = Column(String(30))
    lastName = Column(String(30))
    company = Column(String(100))
    department = Column(String(100))
    jobTitle = Column(String(100))
    city = Column(String(50))
    account = Column(String(20))
    businessPhone = Column(String(50))
    mobile = Column(String(30))
    email = Column(String(30))



def Add(session,contact):
    session.add(contact)
    session.commit()

def BultAdd(session, bultContact):
    session.bulk_save_objects(bultContact)
    session.commit()

def GetDefaultUsr():
    usr = SigContact()
    usr.firstName = ''
    usr.middleName = ''
    usr.lastName = ''
    usr.company = ''
    usr.department = ''
    usr.jobTitle = ''
    usr.city = ''
    usr.account = ''
    usr.businessPhone = ''
    usr.mobile = ''
    usr.email = ''
    return usr

def GetContactFromExcel(fileName):
    book = xlrd.open_workbook('Contact.xls')
    sheet = book.sheet_by_name('Contact')
    contactList = []
    i = 0;
    for row in sheet.get_rows():
        i = i + 1
        if(i>2):
            usr = GetDefaultUsr()
            usr.firstName = row[1]
            usr.middleName = row[2]
            usr.lastName = row[3]
            usr.company = row[5]
            usr.department = row[6]
            usr.jobTitle = row[7]
            usr.city = row[11]
            usr.account = row[48]
            usr.businessPhone = row[31]
            usr.mobile = row[40]
            usr.email = row[59]
            contactList.append(usr)
    return contactList

def DropTable():
    engine = create_engine("mysql+pymysql://root:sMx141110~@localhost:3306/testforwindows", encoding='utf-8',echo=False)
    print(engine)
    base = declarative_base()
    base.metadata.create_all(engine)
    #base.metadata.drop_all()

def CreateTable():
    engine = create_engine("mysql+pymysql://root:sMx141110~@localhost:3306/testforwindows", encoding='utf-8', echo=False)
    base = declarative_base()
    base.metadata.create_all(engine)

if __name__ == '__main__':
    print('Create db table for contact')

    DropTable()
    # session = sessionmaker(bind=engine)()
    # session.query(Contact).first()


    # l = GetContactFromExcel('')
    # print (l.__len__())
    # usr = l[3]
    # print(
    #     usr.firstName ,
    #     usr.middleName ,
    #     usr.lastName ,
    #     usr.company ,
    #     usr.department ,
    #     usr.jobTitle ,
    #     usr.city ,
    #     usr.account ,
    #     usr.businessPhone ,
    #     usr.mobile ,
    #     usr.email ,
    # )
    #BultAdd(session,l)
