import requests
from bs4 import BeautifulSoup as bs
import json
url_first = "https://github.com/login"
post_headers = {

    #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    #"Accept-Encoding": "gzip, deflate, br",
    #"Accept-Language": "en-US,en;q=0.9",
    #"Cache-Control": "max-age=0",
    #"Connection": "keep-alive",
    #"Content-Length": "350",
    #"Content-Type": "application/x-www-form-urlencoded/json",
    #"Cookie": "_octo=GH1.1.1804177316.1569283098; logged_in=no; _ga=GA1.2.1082622240.1569283103; _device_id=4c1d485e322f54cb0af05d003816273e; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=c3lqNW1ROGlFRWNqNEpoVGU4TEVyS1ZybmNOZEhsWnM5L2JqQXRFSGRqZW15YkcweWF3dnlGZXFIVnBoTjNvYkF1dktaUkRYZkpyWDl6djlwckdwS2thZ2FCS2QwaXJDRTNxSXVmakZSQ0pHZ0c2SFU2ZXRUVC9zY1AzZ2VabExFWmd5Mk9pSWtWOWErMEI3Z0ROckc5MFR3b2pSYXI3Tm1DTTA1bTN1YmR3UXpVMUxkSzN4RXFSUzlwZDNLa2dJYmFOS0JNRURtdWl4RDdVem1vU2x6ajQvZVBnMk40bjFYeFZHTWs0VXVpTUJhT0duUE5KMll1ZGNkWGgxVE9IcVYzMTA4UWhHdDdVOXE2U0VzNmhoaXBEeTcyaE5NWXAvTnoyUnRCVDlkQk09LS1XUlJMMVBONUIzSlJQRVU4MTV2bEhBPT0%3D--4c25bb58402957ffa4b4f8ea8284428815a63b22",

    "Host": "github.com",
    #"Origin": "https://github.com",
    "Referer": "https://github.com/",
    #"Sec-Fetch-Mode": "navigate",
    #"Sec-Fetch-Site": "same-origin",
    #"Sec-Fetch-User": "?1",
    #"Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
resp1 = requests.get(url=url_first)

soup = bs(resp1.text,'html.parser')
timestamp = soup.find('input',{'type':'hidden','name':'timestamp'})['value']
timestamp_secret = soup.find('input',{'type':'hidden','name':'timestamp_secret'})['value']
authenticity_token = soup.find('input',{'type':'hidden','name':'authenticity_token'})['value']
required_field = soup.find('input',{'class':'form-control','type':'text','hidden':'hidden'})['name']
#print(resp1.text)
'''
print('timestamp:\t\t\t\t%s'%timestamp)
print('timestamp_secret\t\t%s'%timestamp_secret)
print('authenticity_token\t\t%s'%authenticity_token)
print('required_field\t\t\t%s'%required_field)
'''
url_second = "https://github.com/session"
post_data =  {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": authenticity_token,
            "login": "sunruihua2008@126.com",
            "password": "srh4943868"
                                               
        '''
            "webauthn-support": "supported",
            str(required_field):"",
            "timestamp": timestamp,
            "timestamp_secret": timestamp_secret
        '''
}
sess = requests.Session()
response = sess.post(url=url_second,data= post_data,headers=post_headers)

if(response.status_code==200):
    print(response.text)
else:
    print(response.status_code)


