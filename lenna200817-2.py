import numpy as np
import cv2
from matplotlib import pyplot as plt

# OpenCV는 BGR 모드로 컬러 이미지를 다루는데 반해 Matplotlib은 RGB 모드로 컬러 이미지를 다룬다. 그러므로 제대로 된 컬러가 나오지 않음
img = cv2.imread('images/lenna_256_Color.bmp', cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # Matplotlib은 이미지를 표시할 때 x축 y축으로 눈금 표시를 한다.(소스는 눈금 표시 없이 이미지를 표시)
plt.show()  # 화면에 이미지를 표시
