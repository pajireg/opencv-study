# 47p. affine transformation

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/sudoku_g.png')
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [20, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# pts1의 좌표에 표시. Affine 변환 후 이동 점 확인.
cv2.circle(img, (100, 50), 10, (255, 0, 0), -1)
cv2.circle(img, (200, 50), 10, (0, 255, 0), -1)
cv2.circle(img, (100, 100), 10, (0, 0, 255), -1)

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('image')
plt.subplot(122), plt.imshow(dst), plt.title('Affine')
plt.show()
