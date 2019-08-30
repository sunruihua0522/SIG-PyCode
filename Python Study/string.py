StringX = '0123456789'
print('StringX[1:4]=%s'%(StringX[1:4]))
print('StringX[:4]=%s'%StringX[:4])
print('StringX[-1]=%s'%StringX[-1])
print('StringX[:-2]=%s'%StringX[:-2])
print('StringX[3:-3]=%s'%StringX[3:-3])

StrList=['Hello','HeQing','HengShui','SuZhou','TangShan']
for s in StrList:
    if('S' in s):
        print('%s中包含S'%s)

for c in range(90,100):
    print('%d的字符是%c'%(c,c),end=',')

info='''
    我说"这是一个所见即所得的字符串"
    让程序员从《泥潭》中彻底寄托出来
    \d因为有这个东西很多字符串都不用考虑特殊字符了
'''
print(info)

'''以下测试字符串的内建函数'''
originStr='abcdefgjack'

#首字母大写
print(originStr.capitalize())
print(str.capitalize(originStr))

#要使用str.format，使用字符串的format不能使用
print('{},{},{}'.format(originStr,originStr,originStr))
print(str.format('{0},{1},{2},{3}',originStr,originStr,originStr,originStr))

#使用居中，可以把字符串放在中间位置
print(str.center(originStr,20,'*'))
print(originStr.center(20,'-'))

#使用count来统计出现的次数
print(originStr.count('c',0,-1))
print(originStr.count('c',0,-5))
print(str.count(originStr,'c'))

#判断是否以指定对象结尾
print(originStr.endswith('k'))
print(originStr.endswith(('ack','bck')))

#将字符串中的Tab转为空格
a='abcdefg\tkkllkl\tsfsfsf'
print(a.expandtabs())
print(a)

#虚数  j*j=-1
com=complex(0,1)
print(com*com)
print(com.conjugate())  #实部相等，虚部相反就是共轭复数

#Join函数的使用
print('#'.join((originStr,originStr,'jack')))
print('#'.join(['jiack','luke','lucy']))
print('#'.join(('jiack','luke','lucy')))
print('#'.join('jack'))

#maketrans
tb = str.maketrans('abc','123')
print(originStr.translate(tb))

#title的用法
print('hello yoU are Right'.title())

exit()






