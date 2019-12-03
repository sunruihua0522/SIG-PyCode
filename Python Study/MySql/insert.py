import pymysql
from faker import  Faker
import random

db = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'sMx141110~', db = 'testforwindows', charset = 'utf8')

cur = db.cursor()
sql = '''INSERT INTO customerinfo(C_Index, C_Name, Age, Address, ID,Remark) VALUES (2,"Sunruihua", 32,"HeNan XinYang","20060130522", "GoodMan")'''
#cur.execute(sql)
#db.commit()

try:
    faker1 = Faker()
    for i in range(101,200):
        sql = 'INSERT INTO customerinfo(C_Index, C_Name, Age, Address, ID,Remark) VALUES (%d,"%s", %d,"%s","%s", "%s")'%(i,faker1.name(), random.choice(range(20,60)),faker1.address(),faker1.ssn(), faker1.job())
        cur.execute(sql)
        db.commit()
    print('Insert sucessfully')
except Exception as e:
    db.rollback()
    print(e)
cur.close()
db.close()