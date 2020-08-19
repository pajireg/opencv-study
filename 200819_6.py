# 49p. image perspective
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/sudoku_g.png')
rows, cols = img.shape[:2]

pts1 = np.float32([[0, 0], [244, 0], [0, 255], [244, 255]])
# pts2 = np.float32([[60, 70], [300, 50], [30, 300], [300, 300]])
pts2 = np.float32([[60, 0], [180, 0], [0, 255], [244, 255]])

cv2.circle(img, (100, 50), 5, (255, 0, 0), -1)
cv2.circle(img, (50, 100), 5, (0, 255, 0), -1)
cv2.circle(img, (100, 100), 5, (0, 0, 255), -1)
cv2.circle(img, (50, 50), 5, (0, 255, 255), -1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('image')
plt.subplot(122), plt.imshow(dst), plt.title('Perspective')
plt.show()
