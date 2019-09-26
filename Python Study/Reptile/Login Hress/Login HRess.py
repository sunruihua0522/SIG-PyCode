import requests
from bs4 import BeautifulSoup
sess = requests.Session()

urlPost = 'http://hress.sig.dom/hress/login.php'

url2='http://172.19.10.61:8888/ihrplus_ess/cb_hrms/includes/home_ui.js?_dc=Thu%20Sep%2026%202019%2013:49:53%20GMT+0800%20(China%20Standard%20Time)'

url3='http://172.19.10.61:8888/ihrplus_ess/cb_hrms/index.cfm?event=dynamicGenerateScript.dynamicGenerateScript.dynamicGetAdvFormData&_dc=Thu%20Sep%2026%202019%2016:20:38%20GMT+0800%20(China%20Standard%20Time)'


dataPost = {
'username': 'CN11321',
'password': 'sMx141110~',
'login': 'Login'
}

headerPost = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US,en;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Content-Length': '41',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'hress.sig.dom',
'Origin': 'http://hress.sig.dom',
'Referer': 'http://hress.sig.dom/hress/login.php',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
response = sess.post(url=urlPost,data=dataPost,headers=headerPost)

#get 2
'''
r2 = sess.get(url2)
print(r2.status_code)
#print(r2.text)
'''


#post3

headerPost3 = {
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Origin': 'http://172.19.10.61:8888',
'Referer': 'http://172.19.10.61:8888/ihrplus_ess/cb_hrms/index.cfm?event=hrms.dspHome',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}
dataPost3 = {
    'panel_name': 'my_staff_master_personal'
}

r3 = sess.post(url = url3,data=dataPost3,headers=headerPost3)
if r3.status_code==200:
    print(r3.text)


