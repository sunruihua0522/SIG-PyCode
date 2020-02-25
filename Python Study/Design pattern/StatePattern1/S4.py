from StateBase import StateBase
class S4(StateBase):
    def DoSomething(self,ctx):
        if (ctx.Condition == 6):
            from S5 import S5
            ctx.SetState(S5())
            ctx.DoSomething()
        else:
            print('S4')
