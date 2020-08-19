# 67p. canny edge detection
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/brain.jpg')
# img: canny edge detection 수행할 원본 grayscale 이미지, 30: minimum thresholding value, 70: maximum thresholding value
canny = cv2.Canny(img, 30, 70)

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y', 'Canny']

for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i]), plt.title([titles[i]])
    plt.xticks([]), plt.yticks([])

plt.show()
