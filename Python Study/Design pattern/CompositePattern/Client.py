from Folder import Folder
from SubFile import SubFile

'''
这样也对，真正起作用的是File类，Folder只不过是FIle类的集合而已，不干实事
'''
if __name__ == '__main__':
    folder = Folder('Main folder')
    file = SubFile('File')
    subfolder = Folder('Sub Folder')


    subfolder.AddFile(SubFile('File1'))
    subfolder.AddFile(SubFile('File2'))
    subfolder.AddFile(Folder('Sub Folder 1'))

    folder.AddFile(file)
    folder.AddFile(subfolder)

    folder.DisplayName()