#ecoding=utf-8
class People:
    '所有职业的基类'
    Number = 0
    ChildNumber = 0
    def __init__(self, Name, Salary, IsChild=False):
        if(IsChild):
            People.ChildNumber +=1
        else:
            People.Number =People.Number + 1
        self.Name = Name
        self.Salary = Salary

    def dispInformation(self):
        print('Name:',self.Name, 'Salary', self.Salary)

    def dispCount(self):
        print('People count is %d, Child number is %d' %(People.Number,People.ChildNumber))
class A():
    def eat(self):
        print('A eat')
class B():
    def eat(self):
        print('B eat')

if __name__=='__main__':
    P1= People('HuaGe',10000)
    P1.dispCount()
    P1.dispInformation()
    P2 = People('Tony', 20000)
    P2.dispCount()
    P2.dispInformation()
    P3 = People('胡建东', 5000, IsChild=True)
    P3.dispCount()
    P3.dispInformation()
    P3.Name="刘德华"
    P3.Salary=60000


    P3.Address="香港" #可以动态的添加属性
    P3.dispInformation()
    print(P3.Address)

    del P3.Address  #删除之后就无法访问了
    try:
        print(P3.Address)
    except:
        print('没有Address这个属性')

    '''类可以作为对象'''
    an_list = []
    an_list.append(A)
    an_list.append(B)

    for l in an_list:
        print(l().eat())
    exit(0)

