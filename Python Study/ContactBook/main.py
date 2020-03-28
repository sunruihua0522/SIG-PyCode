from SigContact import SigContact
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import xlrd
#dialect+driver://root:1q2w3e4r5t@127.0.0.1:3306/dbname?charset=UTF8MB4

def Add(session,contact):
    session.add(contact)
    session.commit()

def BultAdd(session, bultContact):
    session.bulk_save_objects(bultContact)
    session.commit()

def GetDefaultUsr():
    usr = SigContact()
    usr.id = 0
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
            usr.firstName = str(row[1].value)
            usr.middleName = str(row[2].value)
            usr.lastName = str(row[3].value)
            usr.company = str(row[5].value)
            usr.department = str(row[6].value)
            usr.jobTitle = str(row[7].value)
            usr.city = str(row[11].value)
            usr.account = str(row[48].value)
            usr.businessPhone = str(row[31].value)
            usr.mobile = str(row[40].value)
            usr.email = str(row[59].value)
            contactList.append(usr)
    return contactList



def CreateTable():
    engine = create_engine("mysql+pymysql://root:sMx141110~@localhost:3306/testforwindows", encoding='utf-8', echo=False)

    base = SigContact()
    # base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    return session


if __name__ == '__main__':
    # try:
    session = CreateTable()

    l = GetContactFromExcel('')
    print (l.__len__())
    usr = l[2]
    print(
        usr.firstName ,
        usr.middleName ,
        usr.lastName ,
        usr.company ,
        usr.department ,
        usr.jobTitle ,
        usr.city ,
        usr.account ,
        usr.businessPhone ,
        usr.mobile ,
        usr.email ,
    )
    # Add(session,l[4])
    BultAdd(session,l)
    # except:
    #     pass
    # finally:
    #     session.close()
