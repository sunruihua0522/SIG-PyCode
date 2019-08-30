class People:
    '这是一个测试类的内置属性的测试'
    PeopleNumber = 0
    def __init__(self, Name, Age, Address='none'):
        People.PeopleNumber += 1
        self.Name = Name
        self.Age = Age
        self.Address = Address

    def __del__(self):
        People.PeopleNumber -=1

    def SayHello(self):
        print('%s say :"Hello everyone, i am %s, i am %d years old, i live in %s"'%(self.Name,self.Name,int(self.Age),self.Address))

    def PrintCount(self):
        print('当前计数%d'%People.PeopleNumber)


if __name__=='__main__':
    P1 = People('孙蓦寻',5,'苏州市吴中区')
    P1.SayHello()

    '''
    下面是类的内置属性的测试
    '''
    print('__doc__: ',P1.__doc__)
    print('__dict__: ', P1.__dict__)
    print('__module__: ', P1.__module__)

    '''测试类的构造与析构函数'''
    P1.PrintCount()
    del P1
    #P1.PrintCount() #此时就会报错，因为P1对象已经被销毁了
    print(People.PeopleNumber)

    exit()