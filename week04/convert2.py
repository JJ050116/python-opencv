# HSV vs RGB 
# RGB = can check one color only
# HSV = can check tone and vibrancy it's multi color

import cv2

img = cv2.imread('./imgs/superman.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, mask = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Original', img)
cv2.imshow('Grayscal', gray)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)

cv2.waitKey(0)
