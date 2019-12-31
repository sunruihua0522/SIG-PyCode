strObj = '我是 python'
print(strObj.encode('utf-16-le'))
print(strObj.encode('gbk'))
print(strObj.encode('utf-8'))

print(strObj.encode('utf-16-le').decode('utf-16-le'))
