import numpy as np
import cv2

img = cv2.imread('images/blue_eye_cat.jpg')
cv2.imshow('full image', img)

roiimg = img[200:380, 300:600]  # [y, x] 200~379 row, 300~599 cols
cv2.imshow('ROI image', roiimg)

img[400:580, 600:900] = roiimg

print(img.shape)
print(roiimg.shape)

cv2.imshow('modified', img)

img[400:580, 300:600] = roiimg

print(img.shape)
print(roiimg.shape)

cv2.imshow('modified', img)

img[400:580, 0:300] = roiimg

print(img.shape)
print(roiimg.shape)

cv2.imshow('modified', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
