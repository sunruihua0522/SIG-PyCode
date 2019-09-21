import IMotion
import xlrd

'''
motion=MotionA.MotionA(name = 'MotionA',color = 'yellow')
motion=MotionB.MotionB('MotionB')
'''

book = xlrd.open_workbook('ini.xlsx')
sheet = book.sheet_by_index(0)
className = sheet.cell_value(0,1)

#反射的关键代码
module_py = __import__(className)
obj_class_name = getattr(module_py,className)
motion = obj_class_name(className)


def Run(motion):
    motion.Run()
    motion.GetInfo()
    motion.GetOil('Qinghai','Henan','HuBei','WuHan','ShenZhen')

if __name__=='__main__':
    Run(motion)

exit()