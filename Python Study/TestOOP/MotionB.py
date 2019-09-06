from IMotion import *

class MotionB(MotionBase):
    def Run(self):
        print('MotionB Run')
    def GetInfo(self):
        print('我的名字叫%s'%(self.Name))

    def GetOil(self, *args):
        sum = []
        for a in args:
            sum.append(a)

        print('%s从加油站%s加的油，加了%d次' % (self.Name,','.join(sum), len(args)))