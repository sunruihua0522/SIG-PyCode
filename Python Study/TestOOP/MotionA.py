from IMotion import*
class MotionA(IMotion):
    def __init__(self,name,age=0,color='red'):
        super(MotionA, self).__init__(name)
        self.Age=age
        self.Color=color
    def Run(self):
        print('MotionA Run')

    def GetInfo(self):
        print('%s的年龄是%d，颜色是%s'%(self.Name,self.Age,self.Color))

    def GetOil(self, *args):
        sum = []
        for a in args:
            sum.append(a)

        print('%s从加油站%s加的油，加了%d次' % (self.Name, ','.join(sum), len(args)))