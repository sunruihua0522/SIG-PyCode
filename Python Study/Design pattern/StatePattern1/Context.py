class Context:
    def __init__(self):
        self.State = None
        pass
    def SetState(self,state):
        self.State = state
    def GetState(self):
        return self.State

    def DoSomething(self):
        self.State.DoSomething(self)