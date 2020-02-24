import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication

from_addr = '715751360@qq.com'
password = 'sxdrgmkcrlhgbffh'
smtp_server = 'smtp.qq.com'
#
# from_addr = 'sunruihua2008@126.com'
# password = 'srh4943868'
# smtp_server = 'smtp.126.com'
#sxdrgmkcrlhgbffh
to_addr =   ['sunruihua2008@126.com','715751360@qq.com','645732822@qq.com']

content ='''
 兔子：
    请检查上封邮件中的信息，及时回复
'''



msg = MIMEMultipart()
msg['From'] = Header('{%s}'%from_addr,'utf-8')
msg['To'] = Header(','.join(to_addr),'utf-8')
msg['Subject'] = Header('开机运行','utf-8')

#文本
attachedFile = MIMEText(content, 'plain', 'utf-8')

# 附件
# attachedFile = MIMEApplication(open('contract.txt','rb').read())
# attachedFile.add_header('Content-Disposition', 'attachment', filename="contract.txt")

#ZIP
# attachedFile = MIMEApplication(open('chromedriver_win32.zip','rb').read())
# attachedFile.add_header('Content-Disposition', 'attachment', filename="chrome.zip")

msg.attach(attachedFile)

#开启发信服务
server = smtplib.SMTP_SSL(smtp_server,465)
#server.connect(smtp_server)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()


