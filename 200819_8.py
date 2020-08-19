# 59p. Opening(erosion -> dilation) and Closing(dilation -> erosion)
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/font.png', cv2.IMREAD_GRAYSCALE)
imgg = cv2.imread('images/font.png')

kernel = np.ones((3, 3), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)

plt.subplot(131), plt.imshow(img), plt.title('Original')
plt.subplot(132), plt.imshow(erosion), plt.title('Erosion')
plt.subplot(133), plt.imshow(dilation), plt.title('Dilation')

plt.show()

img1 = cv2.imread('images/A.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('images/B.png', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)  # 5x5 크기의 1로 채워진 매트릭스를 생성

opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

plt.subplot(221), plt.imshow(img1), plt.title('Original A')
plt.subplot(222), plt.imshow(img2), plt.title('Original B')
plt.subplot(223), plt.imshow(opening), plt.title('Opening')
plt.subplot(224), plt.imshow(closing), plt.title('Closing')

plt.show()
