# 78p. Contour Feature Image Moments
import cv2
import numpy as np

img = cv2.imread('images/bad_rect.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
cv2.drawContours(img, [cnt], 0, (255, 255, 0), 2)   # [cnt]의 모든 픽셀을 두께2, (255,255,0)색 으로 드로잉

M = cv2.moments(cnt)

# contour의 무게주임 x좌표와 y좌표를 구하는 식
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt, True)    # perimeter(둘레), 두번째 파라미터가 True면 폐곡선 False면 열려있는 호

print(M.items()), print(cx, ' ', cy), print(area), print(perimeter)

cv2.imshow('contour', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

