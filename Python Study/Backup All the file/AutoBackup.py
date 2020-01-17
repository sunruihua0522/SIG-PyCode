import sys
sys.path.append('Filler')
sys.path.append('Model')
sys.path.append('Common')

from FileModelMgr import FileModelMgr
from FileOperator import FileOperator
from FillerTime import FillerTime
from FillerFileNumber import FillerFileNumber
from ZipFile import ZipFile

if __name__ == '__main__':
    L = FileModelMgr.getAllFileInfo('File copy list.xlsx')
    L1 = FillerTime(L).ExcuteFiller()
    L2 = FillerFileNumber(L1).ExcuteFiller()

    NeedZipList = list(filter(lambda x: x.Zip == True,L2))
    NotZipList = list(filter(lambda x: x.Zip == False,L2))

    FileOperator.copyFilesToFolder(NotZipList)
    ZipFile.ZipFile(NeedZipList)

    print('done')





