import requests
import urllib
from http import cookiejar
import hashlib
import json
str = 'AaBb141110'
md=hashlib.md5()
md.update(str.encode('utf-8'))
pwd = md.hexdigest()
print(pwd)

url = 'https://www.saikr.com/login'

data = {'name': '13760367706',
        'pass': pwd,
        #'remember': 0
        }

my_agents = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
]
cookies='sk_session=18075d4071385a03a905a2071e0150342cb45905; hdmisaslm=0425cd0cbf4a4cb72e7f9160fc7f4008; Hm_lvt_f0ef5de4e57d9f0a06baad7f2e18ebb3=1569225570,1569302736; Hm_lpvt_f0ef5de4e57d9f0a06baad7f2e18ebb3=1569302736; _msg_lasttime='
headers ={
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '64',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.saikr.com',
    'referer': 'https://www.saikr.com/login',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': my_agents[5],
    'cookie': cookies,
    'x-requested-with': 'XMLHttpRequest'
}

sess = requests.Session()
response = sess.post(url=url,data=data,headers=headers)
if(response.status_code==200):
    print(response.text)
    pass

'''打开我的竞赛界面'''
response = sess.get(url='https://www.saikr.com/u/6092141')


'''打开边界资料界面'''
response = sess.get('https://www.saikr.com/s/p')

print(response.text)




