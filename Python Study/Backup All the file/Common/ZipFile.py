import zipfile
import os
from tqdm import tqdm
class ZipFile:
    @staticmethod
    def zipDir(dirpath,outFullName):
        """
        压缩指定文件夹
        :param dirpath: 目标文件夹路径
        :param outFullName: 压缩文件保存路径+xxxx.zip
        :return: 无
        """
        zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
        for path,dirnames,filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dirpath,'')
            for filename in filenames:
                zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
                #print('%s\r\n%s\r\n\r\n\r\n'%(os.path.join(path,filename),os.path.join(fpath,filename)))
        zip.close()

    @staticmethod
    def ZipFile(fileModelInfoLIst):
        '''
        :param fileModelInfoLIst: -> fileModelInfo of Array
        :return: None
        '''
        for l in fileModelInfoLIst:
            if (l.IsFile()):
                pass
            else:
                print(l.FullName)
                strPre = l.Root.split('\\')[-1]
                if (not os.path.exists(l.PathDes)):
                    os.makedirs(l.PathDes)
                zip = zipfile.ZipFile(os.path.join(l.PathDes, '%s.zip' % strPre), "w", zipfile.ZIP_DEFLATED)
                for path, dirpath, filenames in os.walk(l.FullName):
                    fpath = path.replace(l.FullName, '')
                    for filename in tqdm(filenames):
                        condication1 = len(list(filter(lambda x: x.FullName == path, l.ListIn))) > 0
                        condication2 = len(
                            list(filter(lambda y: os.path.join(path, filename) == y.FullName, l.ListIn))) > 0
                        if (condication1 or condication2):
                            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
                zip.close()
