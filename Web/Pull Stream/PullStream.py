import cv2
#url = 'rtsp://admin:123456@192.168.1.158:8554/11'
#cap = cv2.VideoCapture(url)
cap=cv2.VideoCapture("rtmp://122.51.200.62:1935/hls/room?action=stream")
print(cap.isOpened())
while (cap.isOpened()):
    print(1)
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
