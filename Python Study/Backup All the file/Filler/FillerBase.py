import sys
import datetime
sys.path.append('..\\Model')
from fileModelInfo import fileModelInfo

class FillerBase:
    def __init__(self,fileFullNamesIn):
        self.FileFullNamesIn = fileFullNamesIn
        self._fileFullNamesOut = []
    def ExcuteFiller(self):
        pass