from Context import Context

class StateBase:
    def __init__(self,context):
        context.SetState(self)


    def Run(self):
        pass

    def Stop(self):
        pass

    def Reset(self):
        pass

    def Ready(self):
        pass


