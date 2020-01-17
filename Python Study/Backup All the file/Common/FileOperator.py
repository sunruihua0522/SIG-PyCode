import os
from tqdm import tqdm
import shutil
class FileOperator:
    @staticmethod
    def get_file_list(file_path):
        dir_list = os.listdir(file_path)
        if not dir_list:
            return
        str_list = []
        for l in dir_list:
            str_list.append(os.path.join(file_path, l))
        else:
            # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
            # os.path.getmtime() 函数是获取文件最后修改时间
            # os.path.getctime() 函数是获取文件最后创建时间
            str_list = sorted(str_list, key=lambda x: os.path.getmtime(x), reverse=True)
            # print(dir_list)
            return str_list

    @staticmethod
    def copyFile(filePathSrc,filePathDes):
        shutil.copy(filePathSrc,filePathDes)
    @staticmethod
    def copyFilesToFolder(fileModelInfoList):
        for model in tqdm(fileModelInfoList):
            if(not os.path.exists(model.PathDes)):
                os.makedirs(model.PathDes)
            FileOperator.copyFile(model.FullName,model.PathDes)