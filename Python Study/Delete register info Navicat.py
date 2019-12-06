import winreg

def deleteSubkey(key0, key1, key2=""):
    if key2=="":
        currentkey = key1
    else:
        currentkey = key1+ "\\" +key2

    open_key = winreg.OpenKey(key0, currentkey ,0,winreg.KEY_ALL_ACCESS)
    infokey = winreg.QueryInfoKey(open_key)
    for x in range(0, infokey[0]):
        #NOTE:: This code is to delete the key and all subkeys.
        #  If you just want to walk through them, then
        #  you should pass x to EnumKey. subkey = _winreg.EnumKey(open_key, x)
        #  Deleting the subkey will change the SubKey count used by EnumKey.
        #  We must always pass 0 to EnumKey so we
        #  always get back the new first SubKey.
        subkey = winreg.EnumKey(open_key, 0)
        try:
            winreg.DeleteKey(open_key, subkey)
            print ("Removed %s\\%s " % ( currentkey, subkey))
        except:
            deleteSubkey( key0, currentkey, subkey )
            # no extra delete here since each call
            #to deleteSubkey will try to delete itself when its empty.

    winreg.DeleteKey(open_key,"")
    open_key.Close()
    print ("Removed %s" % (currentkey))
    return

#删除HKEY_CURRENT_USER\SOFTWARE\PremiumSoft
#key = winreg.OpenKey(key = winreg.HKEY_CURRENT_USER,sub_key = 'Software\PremiumSoft', access = winreg.KEY_ALL_ACCESS)

deleteSubkey(winreg.HKEY_CURRENT_USER,'Software\PremiumSoft','Data')


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