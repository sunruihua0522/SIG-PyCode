import requests
import os
from bs4 import BeautifulSoup as bs
import re

'''获取指定页面之间的课程列表'''
def GetCourses(StartPage, EndPage):
    cs=[]
    for i in range(StartPage,EndPage+1):
        txturl = 'https://ke.qq.com/course/list?mt=1001&st=2002&page='+str(i)
        resp = requests.get(txturl)
        txtBs = bs(resp.text,'html.parser')
        list = txtBs.find_all('li',{'class':'course-card-item'})
        matchTxt='class="item-status"'
        count=0
        for l in list:
            g = re.findall(matchTxt,str(l))
            if(g.__len__()!=0):
                count = count + 1
                cs.append(l.h4.a.text)
    return cs

if __name__=="__main__":
    Courses = GetCourses(1,50)
    for c in Courses:
        print(c)
    print(len(Courses))
