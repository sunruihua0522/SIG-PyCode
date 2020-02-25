from StateBase import StateBase
class ReadyState(StateBase):
    def __init__(self, context):
        super(ReadyState, self).__init__(context)

    def Run(self):
        print('机器开始运行')

    def Stop(self):
        print('机器被停止')

    def Reset(self):
        print('机器复位')

    def Ready(self):
        pass

