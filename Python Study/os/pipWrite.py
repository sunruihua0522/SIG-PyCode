import os
import sys

w = os.open('PipTest',os.O_RDWR | os.O_CREAT)
os.write(w,bytes('Hello world','utf-8'))
os.close(w)


sys.exit()

