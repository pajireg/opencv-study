import numpy as np
import cv2

def showImage():
    imgfile = '/images/lenna_256_Color.bmp'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    cv2.imshow('Lenna', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


showImage()
