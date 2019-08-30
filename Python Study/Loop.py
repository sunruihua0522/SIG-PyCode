'''This file is writed to test loop in python'''
for i in range(10,20):
    print(i,)
for _ in range(20,30):
    print('Hello')

x=1
while(x in range(1,20)):
    print('当前的值%d'%x,end='---->')
    x += 1
print(' ')
for c in 'Python':
    if c=='y':
        pass    #pass 什么事情都不干
    print(c, end='---')



exit()