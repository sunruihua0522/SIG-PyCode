class Parent:
    def Talk(self):
        print('Parent Talk')
    def StaticFunc():   #Static method
        print('Parent StaticFunc')
class Child(Parent):
    def Say(self):
        print('Child Say')
    def StaticFunc():
        print('Child StaticFunc')

if __name__=='__main__':
    child=Child()
    # child = Child, it's difference from child = Child()
    child.Say()
    child.Talk()

    Parent.StaticFunc()
    Child.StaticFunc()