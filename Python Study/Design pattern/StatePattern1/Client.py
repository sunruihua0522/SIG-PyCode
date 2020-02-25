from Context import Context
from S1 import S1
if __name__=='__main__':
    ctx = Context()
    ctx.Condition = 2
    ctx.SetState(S1())
    ctx.DoSomething()

    ctx.Condition = 7
    ctx.DoSomething()

    ctx.Condition = 8
    ctx.DoSomething()

    ctx.Condition = 6
    ctx.DoSomething()

    ctx.Condition = 5
    ctx.DoSomething()

    ctx.Condition = 8
    ctx.DoSomething()