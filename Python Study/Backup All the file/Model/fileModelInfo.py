import datetime
import os
class fileModelInfo:
    def __init__(self):
        self.FullName = ''
        self.Descr = ''
        self.PathDes = ''
        self.Enable = False
        self.CopyNumber = -1
        self.Zip = False
        self.Root = 'INVALID_ROOT'

    def IsAvailable(self):
        return os.path.exists(self.FullName)
    def GetSize(self):
        fsize = os.path.getsize(self.FullName)
        fsize = fsize / float(1024 * 1024)
        return round(fsize, 2)
    def GetTailName(self):
        if(self.IsAvailable()):
            return self.FullName.split('\\')[-1]
        return ''
    def IsFile(self):
        return os.path.isfile(self.FullName)

    def GetModifyTime(self):
        t = datetime.datetime.fromtimestamp(os.path.getmtime(self.FullName))
        return t


