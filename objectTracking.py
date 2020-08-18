import cv2
import numpy as np

# Camera 객체를 생성 후 사이즈를 320*240으로 조정
cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 720)

while 1:
    # camera 에서 frame capture
    ret, frame = cap.read()

    if ret:
        # BGR -> HSV 로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # blue 영역의 from ~ to
        lower_blue = np.array([0, 50, 50])
        upper_blue = np.array([15, 255, 255])

        # 이미지에서 blue 영역
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # bit 연산자를 통해서 blue 영역만 남김
        res = cv2.bitwise_and(frame, frame, mask=mask)
        # res = cv2.bitwise_not(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()