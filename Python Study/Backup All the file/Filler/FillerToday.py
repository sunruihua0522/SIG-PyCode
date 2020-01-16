import FillerBase
import datetime
import os
import sys
sys.path.append('..\\Model')
from fileModelInfo import fileModelInfo
class FillerToday(FillerBase.FillerBase):
    def ExcuteFiller(self):
        now = datetime.datetime.now()
        for l in self.FileFullNamesIn:
            if(l.IsFile()):
                t = l.GetModifyTime()
                if (t.year == now.year and t.month == now.month and t.day == now.day):
                    self._fileFullNamesOut.append(l)
            else:
                for path, dir, filenames in os.walk(l.FullName):
                    for file in filenames:
                        model = fileModelInfo()
                        model.FullName = os.path.join(path, file)
                        model.Root = l.Root
                        model.CopyNumber = l.CopyNumber
                        model.Zip = l.Zips
                        model.PathDes = l.PathDes
                        t = model.GetModifyTime()
                        if (t.year == now.year and t.month == now.month and t.day == now.day):
                            self._fileFullNamesOut.append(model)
        return self._fileFullNamesOut
