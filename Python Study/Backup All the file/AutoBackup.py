import os
import time
import datetime
import threading
import zipfile
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
        a.TailName = str(a.FullName.split('\\')[-1]).replace('$COMPUTERNAME$',getComputerName())
        a.PathDes = sheet.cell_value(row, 3)
        a.Available = os.path.exists(a.FullName)
        a.IsFile = os.path.isfile(a.FullName) & a.Available
        if(a.IsFile):
            a.Size = os.path.getsize(a.FullName)
        else:
            a.CopyAll = (sheet.cell_value(row, 5)== 1)
        a.Enable = (sheet.cell_value(row, 4)== 1)
        a.Zip = (sheet.cell_value(row, 6)== 1)
        fileModelList.append(a)

    return fileModelList
def get_FileSize(filePath):
    fsize = os.path.getsize(filePath)
    fsize = fsize / float(1024 * 1024)
    return round(fsize, 2)
def copyFile(filePathSrc,filePathDes):
    shutil.copy(filePathSrc,filePathDes)
def copyFilesInFolder(path,pathDes,copyall=False):
    L = os.listdir(path)
    now = datetime.datetime.now()
    for l in L:
        if(os.path.isfile(os.path.join(path,l))):
            copyFile(os.path.join(path,l),os.path.join(pathDes,l))
        else:
            t = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(path, l)))
            if (not copyall):
                if (not (t.year == now.year and t.month == now.month and t.day == now.day)):
                    continue
            shutil.copytree(os.path.join(path, l), os.path.join(pathDes, l))
def getProgress(filePath):
    fileSize = get_FileSize(filePath)
    size = 0
    while(size<fileSize):
        size = get_FileSize(filePath)
        print('\r%.2f%%'%(100*size/fileSize),end = '',flush=True)
def getComputerName():
    return socket.gethostname()
if __name__ == '__main__':
    L = getAllFileInfo('File copy list.xlsx')
    for l in L:
        print(l.FullName)
        if(l.Enable and l.Available):
            if(l.IsFile):
                copyFile(l.FullName, os.path.join(l.PathDes,l.TailName))
            else:
                if(not os.path.exists(os.path.join(l.PathDes,l.TailName))):
                    os.makedirs(os.path.join(l.PathDes,l.TailName))
                copyFilesInFolder(l.FullName,os.path.join(l.PathDes,l.TailName),l.CopyAll)
    print('done')
    input('Press any key to exit......')


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




