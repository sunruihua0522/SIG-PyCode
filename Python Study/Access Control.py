class Parent:
    def __PrivateMethod(self):
        print('Private method')
    def _ProtectedMethod(self):
        print('Protected method')
    def PublicMethod(self):
        print('Public method')
class Child(Parent):
    pass

if __name__=='__main__':
    c = Child()
    c._ProtectedMethod()  #保护类型只能允许其本身与子类进行访问，不能用于 from module import *
    c.PublicMethod()

    exit()