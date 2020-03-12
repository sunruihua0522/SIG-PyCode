import cv2
import gc
from multiprocessing import Process, Manager,Queue
from threading import Lock
import time
# lock = Lock()

def write(q,cam,top:int):
    cap = cv2.VideoCapture(cam)
    while True:
        if(len(q) < 2):
            res,frame = cap.read()
            if res:
                q.append(frame)
                if(len(q)>2):
                    q.pop(0)



def read(q):
    while True:
        try:
            if(len(q)!=0):
                frame = q.pop(-1)
                cv2.imshow('img',frame)
                print('read')
                key = cv2.waitKey(1)
        except:
            pass


def readDirect():
    cap = cv2.VideoCapture('rtmp://122.51.200.62:1935/hls/room')
    while True:
        if(cap.isOpened()):
            res,frame = cap.read()
            if res:
                cv2.imshow('img',frame)
                key = cv2.waitKey(1)&0xFF
                if(key == ord('q')):
                    break

if __name__ == '__main__':
    # readDirect()
    q = []
    p_write = Process(target=write,args=(q,'rtmp://122.51.200.62:1935/hls/room?action=stream',100))
    p_read = Process(target=read,args=(q,))


    p_write.start()

    p_read.start()

    p_read.join()

    p_write.terminate()