from fake_useragent import UserAgent
import random
import requests
import time
import os
cloth = ['https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-21427681702.3.338d3141AUSRQi&id=596917659477',
         'https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-21427681702.5.338d3141AUSRQi&id=596297739440',
         'https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-21427681702.11.338d3141AUSRQi&id=595129029225',
         'https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-21427681702.17.338d3141AUSRQi&id=593108207387',
         'https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w4004-21427681702.15.338d3141AUSRQi&id=594920023252']
ipList=[]

with open("ip.txt","r") as fr:  #以r形式打开文件
    for line in fr: #一行一行读取
        ipList.append(str(line).replace('\n',''))
print(ipList)

ua = UserAgent(verify_ssl=False)
agent = (ua.random)
headers={'user-agent':agent}

i=0
for ip in ipList:
    try:
        i=i+1
        time.sleep(random.choice(range(10,60)))
        response = requests.get(url=cloth[random.choice(range(0,4))],
                               proxies={'https': ip, 'https': ip},
                               headers=headers
                               )
    except:
        pass
    print(i)
