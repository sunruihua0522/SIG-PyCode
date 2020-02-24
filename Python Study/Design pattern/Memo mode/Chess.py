from Memento import Memento
class Chess:
    def __init__(self, name,x,y):
        self.Name = name
        self._X = x
        self._Y =y
        pass

    def GetX(self):
        return self._X

    def GetY(self):
        return self._Y

    def SetX(self,x):
        self._X = x

    def SetY(self,y):
        self._Y = y

    def Save(self):
        return Memento(self.Name,self.GetX(),self.GetY())

    def Restore(self,memento):
        if(memento != None):
            self.Name = memento.Name
            self._X = memento.X
            self._Y = memento.Y