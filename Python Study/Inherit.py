class People:
    '''这个类是所有职业的基类，这一节主要测试类的继承'''
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    def Information(self):
        '获取People的姓名和年龄'
        print('I am %s, I am %d years old'%(self.Name,self.Age))

class Teacher(People):
    '''所有老师的基类,当子类有__init__的是偶就不会调用父类的'''
    def Teach(self):
        print('Teacher %s is teaching'%self.Name)
class A:
    def MethodA(self):
        print('Method from A')
class B:
    def MethodB(self):
        print('Method from B')

class ColleageTeacher(Teacher,A,B):
    '''具体的大学老师,支持多继承'''
    def __init__(self,Name,Age,Address,IsGood):
        #super(ColleageTeacher,self).__init__(Name,Age)
        Teacher.__init__(self,Name,Age)     #这两种方法都可以
        self.Address = Address
        self.IsGood = IsGood
    def Information(self):
        s ='good' if self.IsGood else 'bad'
        print('I am %s, I am %d years old, i live in %s, i am a %s teacher'%(self.Name,self.Age,self.Address, s))


if __name__=='__main__':
    T1 = ColleageTeacher('Tony.Shi',36, '吴中区', IsGood=True)

    T1.Information()
    T1.Teach()

    T1.MethodA()
    T1.MethodB()

    exit(0)