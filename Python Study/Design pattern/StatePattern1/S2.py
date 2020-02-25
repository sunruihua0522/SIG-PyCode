from StateBase import StateBase
class S2(StateBase):
    def DoSomething(self,ctx):
        if (ctx.Condition == 7):
            from S3 import S3
            ctx.SetState(S3())
            ctx.DoSomething()
        elif (ctx.Condition == 5):
            from S5 import S5
            ctx.SetState(S5())
            ctx.DoSomething()
        else:
            print('S2')
            pass
