from time import time
from CameraBase import CameraBase
class VirtualCamera(CameraBase):
    def __init__(self):
        self.frames = [open(f + '.jpg', 'rb').read() for f in ['1', '2', '3']]


    def get_frame(self):
        return self.frames[int(time()) % 3]