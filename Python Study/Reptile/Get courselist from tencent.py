import requests
import xlwt
from bs4 import BeautifulSoup as bs
import re

'''获取指定页面之间的课程列表'''
def GetCourses(StartPage, EndPage):
    cs=[]
    for i in range(StartPage,EndPage):
        txturl = 'https://ke.qq.com/course/list?mt=1001&st=2002&page='+str(i)
        resp = requests.get(txturl)
        txtBs = bs(resp.text,'html.parser')
        list = txtBs.find_all('li',{'class':'course-card-item'})
        matchTxt='item-line item-line--middle'
        count=0
        for l in list:
            g = re.findall(matchTxt,str(l))
            if(g.__len__()!=0):
                count = count + 1
                cs.append(l.h4.a.text)
    return cs

if __name__=="__main__":
    Courses = GetCourses(51,101)
    book = xlwt.Workbook()
    newSheet = book.add_sheet('Courses')
    row = 0
    for c in Courses:
        newSheet.write(row,0,str(c))
        row = row+1
    book.save('All courses50-100.xlsx')
    print(len(Courses))
