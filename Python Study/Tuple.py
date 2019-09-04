Tup1 = 'a',5,'C','Hello',6.123
#Tup1 = ('a',5,'C','Hello',6.123)
for t in Tup1:
    print (t)

Tup2 = (3,) #记得当只有一个元素的时候要加上逗号，否则会被当作运算符使用
print(Tup2.__len__()) # 1
print(len(Tup2))    # 1

'''We can read tuple, but can not modify it'''
X = Tup1[2]
#Tup1[3]=65.89  we can't modify the tuple.
print(X)

list1 = [1,2,3,4,5,6]
Tup3 = tuple(list1)

print(Tup3)
print(tuple(range(1,10))) #[0,10)


exit()


