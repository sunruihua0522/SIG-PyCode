import math
import random as rd
import cmath    #复数

a=int('FA30',base=16)
print(a)

print(float('30'))

print(math.pi)

print(math.e)

print(pow(2,100))

print(math.sqrt(2))

print(math.exp(2))  #e的多少次幂

print(math.log(100,10)) #以10为底的对数

for _ in range(1,10):
    print(rd.choice(range(1,10)))   #随机挑选


print(list(range(1,10)))    #生成数组
L=list(range(1,10))
rd.shuffle(L)               #随机排序
print(L)

for _ in range(1,10):   #生成随机实数
    print(rd.uniform(1,10))

print(math.trunc(984.6321))
print(math.ceil(984.361))
print(math.floor(984.66654))