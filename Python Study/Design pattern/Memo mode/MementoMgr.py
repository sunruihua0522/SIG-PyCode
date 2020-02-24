class MementoMgr:
    def __init__(self):
        self.MementoList = []

    def AddMemento(self, memento):
        self.MementoList.append(memento)

    def Undo(self):
        if(len(self.MementoList)>0):
            return self.MementoList.pop()