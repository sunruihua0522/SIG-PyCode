import sys
import copy
sys.path.append('..\\Model')
from FileModelInfo import FileModelInfo
from FillerBase import FillerBase
import os

class FillerFileNumber(FillerBase):
    def ExcuteFiller(self):
        for l in self.FileFullNamesIn:
            listIn = l.ListIn
            model = FileModelInfo()
            model.Clone(l)
            if(l.CopyNumber ==-1):  #-1就是全部拷贝
                model._fileFullNamesOut = listIn
            else:
                model.ListIn = copy.deepcopy(sorted(listIn, key = lambda x: x.GetModifyTime(),reverse = True)[:l.CopyNumber])
            self._fileFullNamesOut.append(model)
        return self._fileFullNamesOut
