import os
import sys
sys.path.append('Filler')
#from FillerBase import FillerBase
from FillerToday import FillerToday
from FillerTime import FillerTime
from FillerFileNumber import FillerFileNumber
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
        a.Root = a.FullName
        fileModelList.append(a)
    return fileModelList

def copyFile(filePathSrc,filePathDes):
    shutil.copy(filePathSrc,filePathDes)

def copyFilesToFolder(PathModelList,pathDes):
    for model in PathModelList:
        DesPath = os.path.join(pathDes,str(model.FullPath).replace(model.Root,''))
        if(not os.path.exists(DesPath)):
            os.makedirs(DesPath)
        copyFile(model.FullPath,DesPath)

def getComputerName():
    return socket.gethostname()

if __name__ == '__main__':
    L = getAllFileInfo('File copy list.xlsx')
    L1 = FillerTime(L).ExcuteFiller(360)
    L2 = FillerToday(L1).ExcuteFiller()
    L3 = FillerFileNumber(L2).ExcuteFiller()
    for l in L2:
        print(l.FullName, l.Root, l.CopyNumber, )

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




