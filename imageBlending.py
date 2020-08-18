import numpy as np
import cv2

def nothing(x):
    pass

def imgBlending(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    cv2.namedWindow('Image Blending')
    cv2.createTrackbar('Mixing', 'Image Blending', 50, 100, nothing)
    mix = cv2.getTrackbarPos('Mixing', 'Image Blending')

    while True:
        img = cv2.addWeighted(img1, float(100 - mix) / 100, img2, float(mix) / 100, 0)
        cv2.imshow('Image Blending', img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        mix = cv2.getTrackbarPos('Mixing', 'Image Blending')
    cv2.destroyAllWindows()


imgBlending('images/lena.png', 'images/waterfall.png')
