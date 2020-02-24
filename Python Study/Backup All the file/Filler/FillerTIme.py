from FillerBase import FillerBase
import datetime
import copy
import sys
sys.path.append('..\\Model')
from FileModelInfo import FileModelInfo

class FillerTime(FillerBase):
    def ExcuteFiller(self):
        now = datetime.datetime.now()
        for l in self.FileFullNamesIn:
            listIn = l.ListIn
            model = FileModelInfo()
            model.Clone(l)
            if(l.Time ==-1):  #-1就是全部拷贝
                model._fileFullNamesOut = listIn.copy()
            else:
                model.ListIn= copy.deepcopy(list(filter(lambda x: (now - x.GetModifyTime()).days <= l.Time, listIn)))
            self._fileFullNamesOut.append(model)

        return self._fileFullNamesOut

