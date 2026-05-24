import cv2
import numpy as np

img = cv2.imread('./imgs/superman.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Origin', img)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)

cv2.waitKey(0)

"""
HSV = Hue (Tone of color), Saturation (Vibrancy of color), Value (Brightness)
"""

