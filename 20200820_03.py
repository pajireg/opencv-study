# 80p. Contour Approximation
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/bad_rect.png')
img1 = img.copy()
img2 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]

# 적용하는 숫자가 커질 수록 point의 개수 감소
epsilon1 = 0.01 * cv2.arcLength(cnt, True)  # 오리지널 contour의 둘레 길이의 1%를 epsilon1에 할당
epsilon2 = 0.1 * cv2.arcLength(cnt, True)   # 10%

# cv2.approxPolyDP(): 파라미터로 주어진 곡선 또는 다각형을 epsilon 값에 따라 꼭지점수를 줄여 새로운 곡선이나 다각형을 생성하여 반환
# cnt: Numpy Array 형식의 곡선 또는 다각형. 예제에서 contour를 입력
# epsilon: 근사 정확도를 위한 값
approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)     # 215개의 point
cv2.drawContours(img1, [approx1], 0, (0, 255, 0), 3)     # 21개의 point
cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3)    # 4개의 point

titles = ['Original', '1%', '10%']
images = [img, img1, img2]

for i in range(3):
    plt.subplot(1, 3, i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
