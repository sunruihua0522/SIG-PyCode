import re

print (re.match('www','www.baidu.com').span())

regstr = '^[0-9]*abc$'
print(re.match(regstr,r'6899526abc'))

print(str.center('Test ^ and [] and &',100,'-'))
regstr = '^a[0-9]?abc'
print(re.match(regstr,'a1abc'))

'''re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none'''
print(str.center('Test match',100,'-'))
regstr = '([0-9]*sig$)|(sig[A-Z]?$)'
g = re.match(regstr,'Anj965sig')
print(g)
#print(g.group())
#print(g.group(1))   #返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
print(re.match(regstr,'sig'))


'''re.search 扫描整个字符串并返回第一个成功的匹配'''
print(str.center('Test search',100,'-'))
regstr ='sig[A-Z]+'
print(re.search(regstr,'Anj965sigH8sig'))


'''在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
注意： match 和 search 是匹配一次 findall 匹配所有。'''
print(str.center('Test findall',100,'-'))
regstr ='sig[A-Z]+'
print(re.findall(regstr,'Anj965sigH8sigOKLopiojisigPlkj'))

cmp = re.compile(regstr)
print(cmp.findall('Anj965sigH8sigOKLopiojisigPlkj'))


'''re.finditer 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。'''
regstr ='sig[A-Z]+'
cmp = re.compile(regstr)
it = cmp.finditer('Anj965sigH8sigOKLopiojisigPlkj')
for match in it:
    print(match.group())

'''re.split ,split 方法按照能够匹配的子串将字符串分割后返回列表'''
regstr ='sig[A-Z]+'
cmp = re.compile(regstr)
print(cmp.split('Anj965sigH8sigOKLopiojisigPlkj'))


exit()