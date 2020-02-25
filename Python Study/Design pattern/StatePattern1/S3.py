from StateBase import StateBase
class S3(StateBase):
    def DoSomething(self,ctx):
        if (ctx.Condition == 8):
            from S4 import S4
            ctx.SetState(S4())
            ctx.DoSomething()
        else:
            print('S3')

