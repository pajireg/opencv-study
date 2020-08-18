import numpy as np
import cv2


def showImage():
    imgfile = 'images/lenna_256_Color.bmp'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.namedWindow('Lenna', cv2.WINDOW_AUTOSIZE)  # WINDOW_AUTOSIZE: 크기 고정, WINDOW_NORMAL:크기 조정
    cv2.imshow('Lenna', img)

    # k = cv2.waitKey(0) & 0xFF   # 64비트에서 0xFF를 &연산
    #
    # if k == 27:
    #     cv2.waitKey(0) # 키보드 입력이 있을때까지 기다리려라
    # elif k == ord('c'): # ord(): 문자를 아스키 값으로 반환, c키를 누르면 이미지 복사 후 닫기
    #     cv2.imwrite('images/lenna_copy.png', img)
    #     cv2.destroyAllWindows()
    while True:
        k = cv2.waitKey(0) & 0xFF
        if k == 27:  # ESC Ascii code
            break
        elif k == ord('c'):
            cv2.imwrite('images/lenno_copy.png', img)
        else:
            print('esc나 c키를 누르세요.')

    cv2.destroyAllWindows()


showImage()
