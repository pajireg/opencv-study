import cv2

img = cv2.imread('images/global.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold 를 이용하여 binary image로 변환
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

# contours는 point의 list형태

# hierachy는 contour line의 계층 구조
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1, (0, 0, 255), 1)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 동영상을 가져와서 피부색사응로 따서 배경 이미지 위에 띄우기
