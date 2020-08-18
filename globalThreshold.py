import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/gradient.png')
# cv2.threshold(img, threshold_value, value, flag)
# threshold_value: 픽셀 임계치, value: 픽셀 임계치보다 클 때 적용되는 최대값, flag: 임계치 적용 방법 또는 스타일
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # 픽셀 값이 threshold_value 보다 크면 value, 작으면 0
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)  # 픽셀 값이 threshold_value 보다 크면 0, 작으면 0
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)   # 픽셀 값이 크면 threshold_value, 작으면 셀값 그대로 할당
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)  # 크면 그대로, 작으면 0
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # 크면 0, 작으면 픽셀 값 그대로

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

