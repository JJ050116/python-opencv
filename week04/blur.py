import cv2 

img = cv2.imread('./imgs/superman.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# .GaussianBlur() = 1. input 2. (kernel <odd numeric>) 3. rubbing
# kernel = size of image for blur 11x11 (if kernel greater means more blur)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

# .Canny() = drawing line value btween color conflict
edges = cv2.Canny(blurred, 10, 150)

cv2.imshow('blurred', blurred)
cv2.imshow('Smooth Edges', edges)
cv2.waitKey(0)