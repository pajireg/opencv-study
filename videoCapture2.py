import cv2

# cap = cv2.VideoCapture('videos/file_example_AVI_480_750kB.avi')
cap = cv2.VideoCapture('videos/file_example_AVI_1280_1_5MG.avi')

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(cap.get(3))   # 파일 너비
print(cap.get(4))   # 파일 높이

cap.release()
cv2.destroyAllWindows()
