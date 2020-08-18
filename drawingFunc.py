import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)   # 좌표 (0,0)에서 (511,511)까지 파란색의 두께 5인 직선을 그림
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)    # 좌측상단(384,0)에서 우측하단(510,128)까지 녹색의 두께 3인 직선
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1) # 원의중심(447,63)
# cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
# cv2.polylines(img, [pts], True, (0, 255, 255))

font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('Drawing', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
