# 44p. image resizing

import cv2
import numpy as np

img = cv2.imread('images/opencv-logo-white.png')

# 행: Height, 열: width
height, width = img.shape[:2]   # img.shape[:2] = 2개, img.shape[:] = 3개

# 이미지 축소
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Manual Size 지정
zoom1 = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

# 배수 Size 지정
zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Original', img)
cv2.imshow('Shrink', shrink)
cv2.imshow('zoom1', zoom1)
cv2.imshow('zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()