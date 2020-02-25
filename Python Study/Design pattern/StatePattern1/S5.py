from StateBase import StateBase
class S5(StateBase):
    def DoSomething(self,ctx):
        if(ctx.Condition == 5):
            from S3 import S3
            ctx.SetState(S3())
            ctx.DoSomething()
        else:
            print('S5')

