import sys
sys.path.append('..\\')
from fileModelInfo import fileModelInfo
from FillerBase import FillerBase
import os
class FillerFileNumber(FillerBase):
    def ExcuteFiller(self):
        rootDic = {}
        for l in self.FileFullNamesIn:
            if(not l.Root in rootDic):
                rootDic.update({l.Root:l.CopyNumber})

        for k,v in rootDic.items():
            list = self.get_file_list(k)
            for i in range(0,len(list)):
                if (v==-1):
                    pass
                else:
                    if(i < v):
                        model = fileModelInfo()
                        model.FullName = list[i]
                        model.Root = k
                        model.CopyNumber = v
                        self._fileFullNamesOut.append(model)

        return self._fileFullNamesOut


    def get_file_list(self,file_path):
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        str_list = []
        for l in dir_list:
            d = list(filter(lambda x: x.GetTailName == l,self.FileFullNamesIn))
            if(not d):
                if(os.path.isfile(os.path.join(file_path,l))):
                    str_list.append(os.path.join(file_path,l))
        else:
            # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
            # os.path.getmtime() 函数是获取文件最后修改时间
            # os.path.getctime() 函数是获取文件最后创建时间
            str_list = sorted(str_list,key=lambda x: os.path.getmtime(x), reverse=True)
            # print(dir_list)
            return str_list