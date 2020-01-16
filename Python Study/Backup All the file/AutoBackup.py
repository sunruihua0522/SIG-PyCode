import os
import sys
import zipfile
sys.path.append('Filler')
sys.path.append('Model')
sys.path.append('Common')
#from FillerBase import FillerBase
from FillerToday import FillerToday
from FillerTime import FillerTime
from FillerFileNumber import FillerFileNumber
from ZipFile import ZipFile
import socket
import xlrd
import shutil
from fileModelInfo import fileModelInfo
from tqdm import tqdm
fileSize = 0

def getAllFileInfo(excelFilePath):
    fileModelList = []
    book = xlrd.open_workbook(excelFilePath)
    sheet = book.sheet_by_index(0)
    for row in range(1, sheet.nrows):
        a = fileModelInfo()
        a.Descr = str(sheet.cell_value(row, 1)).replace('$COMPUTERNAME$',getComputerName())
        a.FullName = str(sheet.cell_value(row, 2)).replace('$COMPUTERNAME$',getComputerName())
        a.PathDes = sheet.cell_value(row, 3)
        a.Enable = (sheet.cell_value(row, 4) == 1)
        if(not a.IsFile()):
            a.CopyNumber = int(sheet.cell_value(row, 5))
        else:
            a.CopyNumber = -1

        a.Zip = (sheet.cell_value(row, 6)== 1)
        if(not a.IsFile()):
            a.Root = a.FullName
        else:
            a.Root = 'INVALID_ROOT'

        fileModelList.append(a)
    return fileModelList

def copyFile(filePathSrc,filePathDes):
    shutil.copy(filePathSrc,filePathDes)

def copyFilesToFolder(fileModelInfoList):
    for model in fileModelInfoList:
        if(not os.path.exists(model.PathDes)):
            os.makedirs(model.PathDes)
        copyFile(model.FullName,model.PathDes)

zipPathDic = {}
def ZipAllFile(fileModelInfoLIst):
    for l in fileModelInfoLIst:
        if(not l.Root in zipPathDic):
            zipPathDic.update({l.Root:l.Zip})
    for k,v in zipPathDic.items():
        if(v):
            L = list(filter(lambda x: x.Root == k,fileModelInfoLIst))
            if(len(L)>0):
                strPre = L[0].Root.split('\\')[-1]
                zip = zipfile.ZipFile(os.path.join(L[0].PathDes,'%s.7z'%strPre), "w", zipfile.ZIP_DEFLATED)
                for m in L:
                    zip.write(m.FullName,m.GetTailName())
                zip.close()

def getComputerName():
    return socket.gethostname()

if __name__ == '__main__':
    L = getAllFileInfo('File copy list.xlsx')
    L1 = FillerTime(L).ExcuteFiller(360)

    #for l in L:
    #    print(l.FullName, l.CopyNumber, l.Zip)
    L2 = FillerFileNumber(L1).ExcuteFiller()

    NeedZipList = list(filter(lambda x: x.Zip == True,L2))
    NotZipList = list(filter(lambda x: x.Zip == False,L2))


    ZipAllFile(NeedZipList)
    copyFilesToFolder(NotZipList)


    '''
    t1 = threading.Thread(target = copyFile, kwargs={'filePathSrc':'D:\\Software\\HALCON17.12.0.0\\halcon-17.12.0.0-windows.exe','filePathDes':'D:\\a.exe'})
    t2 = threading.Thread(target = getProgress, kwargs = {'filePath':'D:\\a.exe'})
    t1.start()
    time.sleep(1)
    t2.start()
    t2.join()
    t1.join()
    print('\r\n---------------------------------------')
    '''




