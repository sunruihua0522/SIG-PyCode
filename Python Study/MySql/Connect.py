import pymysql

coon = pymysql.connect(host = 'localhost', user = 'root',passwd = 'sMx141110~',
                       port = 3306, db = 'testforwindows',charset = 'utf8')
cur = coon.cursor()  #建立游标
cur.execute("select * from CustomerInfo")  #查询数据
res = cur.fetchall()    #获取结果
print(res)
cur.close()     #关闭游标
coon.close()    #关闭连接


