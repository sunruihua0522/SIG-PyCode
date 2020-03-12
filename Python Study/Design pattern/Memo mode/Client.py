from MementoMgr import MementoMgr
from Chess import Chess

MetoMgr = MementoMgr()
def play(chess):
    MetoMgr.AddMemento(chess.Save())
    print('当前棋子%s, 位置(%d,%d)'%(chess.Name,chess.GetX(),chess.GetY()))

def UnDo(chess):
    chess.Restore(MetoMgr.Undo())
    print('悔棋—》 棋子%s,位置(%d,%d)' % (chess.Name, chess.GetX(), chess.GetY()))

if __name__=='__main__':
    c = Chess('马',2,2)
    play(c)
    c.SetX(10)
    play(c)
    c.SetY(7)
    play(c)

    UnDo(c)
    UnDo(c)
    UnDo(c)
    UnDo(c)
    UnDo(c)
    UnDo(c)
    UnDo(c)
    pass