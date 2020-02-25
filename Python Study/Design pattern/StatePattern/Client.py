from StateBase import StateBase
from Context import Context
from RunningState import RunningState
from StopState import StopState
from ResetState import ResetState
from ResetState import ResetState

if __name__=='__main__':
    context = Context()
    state = ResetState(context)

    context.Run()
    context.Stop()
    context.Reset()
    context.Ready()
