import requests
from bs4 import BeautifulSoup

post_url = 'https://passport.csdn.net/v1/register/pc/login/doLogin'

post_header = {
'accept': 'application/json, text/plain, */*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'content-length': '82',
'content-type': 'application/json;charset=UTF-8',
'cookie': 'uuid_tt_dd=10_30269814540-1569331216197-264284; dc_session_id=10_1569331216197.215185; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_30269814540-1569331216197-264284!1788*1*PC_VC; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1569468897,1569468981,1569469045,1569473893; c-login-auto=13; SESSION=cea49b50-a6b2-408d-aefb-cfd7de31700d; dc_tos=pyhf5f',
'origin': 'https://passport.csdn.net',
'referer': 'https://passport.csdn.net/login?code=public',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
'x-requested-with': 'XMLHttpRequest'
}

post_data = {
'loginType': "1",
'pwdOrVerifyCode': "123456789",
'userIdentification': "13760367706"
}

sess = requests.Session()
r = requests.post(url=post_url, data = post_data, headers = post_header)

if(r.status_code==200):
    print(r.text)
print (r.text)