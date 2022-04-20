import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

import numpy as np
import cv2

# cap = cv.VideoCapture('rtsp://192.168.0.2:8554/')
capture = cv2.VideoCapture('D:\Downloads\People-84973.mp4')
 
while capture.isOpened():
    run, frame = capture.read()
    if not run:
        print("[프레임 수신 불가] - 종료합니다")
        break
    img = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    cv2.imshow('video', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
 
capture.release()
cv2.destroyAllWindows()