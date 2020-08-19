# 카메라를 받아서 perspective 변환하여 프레임 단위로 이미지 변환
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 720)

pts1 = np.float32([[0, 0], [244, 0], [0, 255], [244, 255]])
pts2 = np.float32([[60, 0], [180, 0], [0, 255], [244, 255]])

while 1:
    # camera 에서 frame capture
    ret, frame = cap.read()

    img = cv2.imread(frame)
    rows, cols = img.shape[:2]

    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, M, (cols, rows))

    cv2.imshow('frame', frame)
    cv2.imshow('perspective', dst)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
