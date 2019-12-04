import winreg

#删除HKEY_CURRENT_USER\SOFTWARE\PremiumSoft
key = winreg.OpenKey(key = winreg.HKEY_CURRENT_USER,sub_key = 'Software\PremiumSoft', access = winreg.KEY_ALL_ACCESS)
try:
    clsid = 0
    while(1):
        x = winreg.EnumKey(key,clsid)
        print('remiumSoft的子键',x)
        if(x.lower()=='data'):
            winreg.DeleteKey(key, 'Data')
        clsid += 1
except Exception as e:
    print(e)



#删除所有的Info子键
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\Classes\CLSID')
try:
    i = 0
    while(1):
        #EnumValue方法用来枚举键值，EnumKey用来枚举子键
        subkey = winreg.EnumKey(key, i)
        #print('''%s\t\t:Value%s  %s'''%(name,value,type))
        print(subkey)
        subkey = winreg.OpenKey(key, subkey)
        try:
            j = 0
            while(1):
                childkeyStr = winreg.EnumKey(subkey,j)
                print('---',childkeyStr)
                if(childkeyStr.lower() == 'info'):
                    winreg.DeleteKey(subkey,childkeyStr)
                    print('######################################')
                j+=1
        except:
            pass
        i +=1
except Exception as e:
    pass