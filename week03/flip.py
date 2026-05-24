import cv2

img = cv2.imread('imgs/images.jpeg')

# .filp() = 1. image (input) 2. 1: (left or right) 0: (top or bottom)
img_flip = cv2.flip(img, 0)

cv2.imshow('Flip', img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()