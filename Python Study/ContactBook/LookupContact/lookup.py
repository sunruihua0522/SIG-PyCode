import sys
sys.path.append('../')
from SigContact import SigContact
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:sMx141110~@localhost:3306/testforwindows", encoding='utf-8',
                           echo=False)
    base = SigContact()
    base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()


    # user = session.query(SigContact).filter(SigContact.id == '5').one()
    user = session.query(SigContact).filter(SigContact.firstName.like('%ruihua%')).one()
    print(user.mobile, user.email, user.businessPhone)

    session.close()