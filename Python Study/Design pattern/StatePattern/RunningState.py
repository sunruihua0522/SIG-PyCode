from StateBase import StateBase
class RunningState(StateBase):
    def __init__(self, context):
        super(RunningState, self).__init__(context)

    def Run(self):
        pass

    def Stop(self):
        print('机器被停止')

    def Reset(self):
        pass

    def Ready(self):
        pass