dic = {'tiny':10, 1:2, 26.0:89, (1,2,5,9,):'tuple'}
print(dic)

for k in dic.keys():
    print(k)
for v in dic.values():
    print(v)
for k,v in dic.items():
    print(k,'------------',v)