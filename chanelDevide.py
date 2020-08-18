# import numpy as np
# import cv2
#
# img = cv2.imread('images/lenna_256_Color.bmp')
#
# b, g, r = cv2.split(img)
#
# print(img[100, 100])
# print(b[100, 100], g[100, 100], r[100, 100])
#
# cv2.imshow('Blue Channel', b)
# cv2.imshow('Green Channel', g)
# cv2.imshow('Red Channel', r)
#
# merged_img = cv2.merge((b, g, r))
# cv2.imshow('merged', merged_img)
#
# b2 = img[:, :, 0]
# g2 = img[:, :, 1]
# r2 = img[:, :, 2]
#
# # cv2.imshow('Blue 2', b2)
# # cv2.imshow('Green 2', g2)
# # cv2.imshow('Red 2', r2)
#
# merged2 = cv2.merge((g2, r2, b2))
# cv2.imshow('merged2', merged2)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

## 더하기

import numpy as no
import cv2


def addImage(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.imshow('lena', img1)
    cv2.imshow('waterfall', img2)

    add_img1 = img1 + img2  # 더한 값이 255보다 크면 256으로 나눈 나머지 값 지정
    add_img2 = cv2.add(img1, img2)  # 더한값이 255보다 크면 255으로 값 지정

    cv2.imshow('lena + waterfall', add_img1)
    cv2.imshow('add(lena, waterfall)', add_img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


addImage('images/lena.png', 'images/waterfall.png')
