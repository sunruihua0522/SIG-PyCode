import cv2
from CameraBase import CameraBase
class StreamCamera(CameraBase):
    def __init__(self):
        # 通过opencv获取实时视频流
        url = "rtmp://122.51.200.62:1935/hls/room?action=stream"
        self.video = cv2.VideoCapture(url)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # 因为opencv读取的图片并非jpeg格式，因此要用motion JPEG模式需要先将图片转码成jpg格式图片
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()