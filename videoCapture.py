import numpy as np
import cv2

cap = cv2.VideoCapture(0)   # 파라미터로 장치 인덱스를 지정(PC에 웹캠이 2개이상 있는 경우 첫번째 웹캠은 0, 두번쨰 웹캠은 1)
# 또한 저장된 비디오파일을 재생하려면 비디오파일 경로와 함께 지정 ex) cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)  # 원래 컬러

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
