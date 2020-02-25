from StateBase import StateBase
class StopState(StateBase):
    def __init__(self, context):
        super(StopState, self).__init__(context)
    def Run(self):
        pass

    def Stop(self):
        pass

    def Reset(self):
        print('机器复位')

    def Ready(self):
        pass