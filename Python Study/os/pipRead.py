import os
import sys

r = os.open('PipTest',os.O_RDWR | os.O_CREAT)
print(os.read(r,100))
os.close(r)

sys.exit()