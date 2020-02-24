import pymysql
coon = pymysql.connect(host = 'localhost', user = 'root',passwd = 'sMx141110~',
                       port = 3306, db = 'testforwindows',charset = 'utf8')

cur = coon.cursor()  #建立游标
sql = 'update customerinfo set C_Name = "Sunruihua" where C_Index = 101'


cur.execute(sql)


coon.commit()

cur.close()
coon.close()