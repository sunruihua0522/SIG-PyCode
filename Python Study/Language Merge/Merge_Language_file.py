import xlrd
import os
import operator as op
def is_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def get_strList(excelfileName):
    L=[]
    path = ''
    splitpath = str(__file__).split('/')
    print(splitpath)
    for i in range(0, len(splitpath) - 1):
        path = path + splitpath[i] + '\\'
    print(path)
    book = xlrd.open_workbook(os.path.join(path, excelfileName))
    sheet = book.sheet_by_index(0)
    for i in range(1, sheet.nrows):
        L.append(sheet.cell_value(i,1).strip())
    return L

def is_contain_special_string(check_str,L):
    return (check_str in L)


f1 = open("CHINESE.txt",encoding="utf-16-le")
f2 = open("CHINESE1.txt",encoding="utf-16-le")
strList = get_strList('strList.xlsx')
lines1 = f1.readlines()
lines2 = f2.readlines()
textList=[]
name =''
value = ''
print('正在处理......')
changeList =[]
for line1 in lines1:
    L1=line1.split('|')
    if(len(L1)!=2):
        #print('*******************************')
        continue
    name = L1[0]
    value = L1[1]
    lineNum=0
    for line2 in lines2:
        L2 = line2.split('|')
        lineNum=lineNum+1
        if(len(L2)!=2 ):
            #print('############################  %d 行号%d'%(len(L2),lineNum))
            continue
        name2 = L2[0]
        if(name.strip() == name2.strip()):
            if(not op.eq(L1[1].strip(),L2[1].strip())):
                if (is_contain_chinese(L2[1].strip()) and not is_contain_special_string(L2[1].strip(),strList)):
                    value = L2[1]
                    word = ('%s:\t %s————————>%s\r\n'%(name,L1[1],L2[1]))
                    changeList.append(word)
                    print(name)
            break
    textList.append('%s|%s'%(name,value))
    
print('%d items had been changed:'%len(changeList))

#write log
file = open('log.txt',encoding="utf-8",  mode='w')
for c in changeList:
    file.write(c)

#write new file
file = open('new.txt', encoding="utf-16-le", mode='w')
for x in textList:
      file.write(x) 
                       
print('Done!')
input('Pess any key to close')

