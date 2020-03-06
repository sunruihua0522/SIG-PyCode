import cv2
cap = cv2.VideoCapture(0)
width = 640
height = 480
w = 360
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

crop_w_start = (width-w)//2
crop_h_start = (height-w)//2
ret, frame = cap.read()
# show a frame
frame = frame[crop_h_start:crop_h_start+w, crop_w_start:crop_w_start+w]
frame = cv2.flip(frame,1,dst=None)
cv2.imshow("capture", frame)

cap.release()
cv2.destroyAllWindows()

