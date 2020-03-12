class Folder:
    def __init__(self,name):
        self.Name = name
        self.FolderList = []

    def AddFile(self,folder):
            self.FolderList.append(folder)

    def DeleteFile(self,folder):
            self.FolderList.remove(folder)

    def DisplayName(self):
        for f in self.FolderList:
            f.DisplayName()

