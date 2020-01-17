import sys
sys.path.append('..\\Common')
from FileModelInfo import FileModelInfo
from FileOperator import FileOperator
import socket
import xlrd
class FileModelMgr:
    @staticmethod
    def getAllFileInfo(excelFilePath):
        fileModelList = []
        book = xlrd.open_workbook(excelFilePath)
        sheet = book.sheet_by_index(0)
        for row in range(1, sheet.nrows):
            a = FileModelInfo()
            a.Descr = str(sheet.cell_value(row, 1)).replace('$COMPUTERNAME$', FileModelMgr.getComputerName())
            a.FullName = str(sheet.cell_value(row, 2)).replace('$COMPUTERNAME$', FileModelMgr.getComputerName())
            a.PathDes = sheet.cell_value(row, 3)
            a.Enable = (sheet.cell_value(row, 4) == 1)
            if (not a.IsFile()):
                a.CopyNumber = int(sheet.cell_value(row, 5))
            else:
                a.CopyNumber = -1
            if (not a.IsFile()):
                fileList = FileOperator.get_file_list(a.FullName)
                for f in fileList:
                    x = FileModelInfo()
                    x.FullName = f
                    a.ListIn.append(x)
            a.Zip = (sheet.cell_value(row, 6) == 1)

            if (not a.IsFile()):
                a.Root = a.FullName
            else:
                a.Root = 'INVALID_ROOT'
            a.Time = sheet.cell_value(row, 7)
            if (a.Enable):
                fileModelList.append(a)
        return fileModelList
    @staticmethod
    def getComputerName():
        return socket.gethostname()