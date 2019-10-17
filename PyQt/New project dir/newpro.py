import os
import sys
import datetime
def makeSubDir(fatherPath):
    currentPath = fatherPath
    d1 = ['Backup\Counter','Backup/HMI/IPA','Backup/HMI/Recipes','Backup/HMI/RT','Backup/HMI/ScreenShot',
          'Backup/PLC/SourceUpload','Backup/Problem','Backup/SaveMachineData','Backup/US']
    for s in d1:
        d = '%s/%s'%(currentPath,s)
        if(not os.path.exists(d)):
            os.makedirs(d)
def makedir():
    length = len(sys.argv)
    now = datetime.datetime.now().date()
    if(length>1):
        currentPath = '%s %d_%d_%d'%(sys.argv[1],now.year,now.day,now.day)
        if (not os.path.exists(currentPath)):
            os.makedirs('%s/Reimburse' % (currentPath))
            os.makedirs('%s/Report' % (currentPath))
            os.makedirs('%s/UpdateKit/PLC_Source' % (currentPath))
            if(length == 2):
                makeSubDir(currentPath)
            if(length>2):
                for i in range(2,length):
                    subDir = '%s/%s'%(currentPath,sys.argv[i])
                    print(subDir)
                    makeSubDir(subDir)
if __name__=='__main__':
    makedir()
