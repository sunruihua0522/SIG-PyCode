from StateBase import StateBase
class S1(StateBase):
    def DoSomething(self,ctx):
        if (ctx.Condition == 1):
            from S4 import S4
            ctx.SetState(S4())
            ctx.DoSomething()
        elif (ctx.Condition == 2):
            from S2 import S2
            ctx.SetState(S2())
            ctx.DoSomething()
        elif (ctx.Condition == 4):
            from S5 import S5
            ctx.SetState(S5())
            ctx.DoSomething()
        else:
            print('S1')
            pass


