import cv2

img = cv2.imread('imgs/images.jpeg')

if img is None:
    print('Cloud not found read the images.')

# gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

saveNew = cv2.imwrite('grayscale.jpeg', gray)
newFile = cv2.imread('grayscale.jpeg')

cv2.imshow('GrayScale', newFile)
cv2.waitKey(0)
cv2.destroyAllWindows()