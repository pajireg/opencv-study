# 100p. image histogram
import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img1 = cv2.imread('images/brain.jpg', 0)
img2 = cv2.imread('images/blue_eye_cat.jpg', 0)

# cv2.calcHist(img, channel, mask, histSize, range): 이미지 히스토그램을 찾아서 numpy 배열로 반환
# mask: 이미지 전체에 대한 히스토그램을 구할경우 None, 특정 영역의 히스토그램을 구할 경우 이 영역에 해당하는 mask값을 입력
# histSize: BIN 개수, 파라미터는 []로 둘러싸야 함
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

plt.subplot(221), plt.imshow(img1, 'gray'), plt.title('Red Line')
plt.subplot(222), plt.imshow(img2, 'gray'), plt.title('Green Line')
plt.subplot(223), plt.plot(hist1, color='r'), plt.plot(hist2, color='g')
plt.xlim([0, 256])
plt.show()

