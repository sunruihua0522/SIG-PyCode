from FillerBase import FillerBase
import datetime
import sys
sys.path.append('..\\Model')
from fileModelInfo import fileModelInfo
import os
class FillerTime(FillerBase):
    def ExcuteFiller(self,timeInDays):
        now = datetime.datetime.now()
        for l in self.FileFullNamesIn:
            if(l.IsFile()):
                t = l.GetModifyTime()
                difference = now - t
                if(difference.days <= timeInDays):
                    self._fileFullNamesOut.append(l)
            else:
                for path, dir, filenames in os.walk(l.FullName):
                    for file in filenames:
                        model = fileModelInfo()
                        model.FullName = os.path.join(path, file)
                        model.Root = l.Root
                        model.CopyNumber = l.CopyNumber
                        model.Zip = l.Zip
                        model.PathDes = l.PathDes
                        t = model.GetModifyTime()
                        difference = now - t
                        if (difference.days <= timeInDays):
                            self._fileFullNamesOut.append(model)
        return self._fileFullNamesOut