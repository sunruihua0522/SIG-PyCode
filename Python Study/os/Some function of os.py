import os
print(os.getcwd())

print(os.getcwdb())

if(not os.path.exists('D:/Test/Test1/Test2/Test3')):
    os.makedirs('D:/Test/Test1/Test2/Test3')
for f in os.walk('D:/Test'):
    print(str(f))



exit()