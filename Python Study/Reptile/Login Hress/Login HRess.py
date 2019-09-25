import requests
from bs4 import BeautifulSoup
sess = requests.Session()

urlPost = 'http://hress.sig.dom/hress/login.php'
url2='http://172.19.10.61:8888/ihrplus_ess/cb_hrms/index.cfm?event=hrms.dspHome'
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
#'Cookie': 'PHPSESSID=637p7m6kbnd8d743rfj6rcqcn0',
'Host': 'hress.sig.dom',
'Origin': 'http://hress.sig.dom',
'Referer': 'http://hress.sig.dom/hress/login.php',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
response = sess.post(url=urlPost,data=dataPost,headers=headerPost)

#print(response.text)
headerPos2 = headerPost
headerPos2['cookie'] = 'CFID=319dbfea-cfb9-4d5e-8cc8-5ba012b74fb3; CFTOKEN=0; USERNAME=25DAD607; CURRENT_LANG=26D9D6'
dataPost2 = {
    'personal_code': 'MTQ0MzQy',
    'submit': 'enter'
}
r1 = sess.post(url = url2,data=dataPost2,headers=headerPos2)


print(r1.text)