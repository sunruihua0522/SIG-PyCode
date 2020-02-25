class Context:
    def __init__(self):
        self.State = None

    def SetState(self, state):
        self.State = state

    def GetState(self):
        return self.State


    def Run(self):
        self.State.Run()

    def Stop(self):
        self.State.Stop()

    def Reset(self):
        self.State.Reset()

    def Ready(self):
        self.State.Ready()