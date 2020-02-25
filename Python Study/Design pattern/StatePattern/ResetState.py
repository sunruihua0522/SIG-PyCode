from StateBase import StateBase
class ResetState(StateBase):
    def __init__(self,context):
        super(ResetState,self).__init__(context)


    def Run(self):
        pass

    def Stop(self):
        print('机器被停止')

    def Reset(self):
        pass

    def Ready(self):
        print('机器就绪')