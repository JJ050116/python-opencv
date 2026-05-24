# calling a module or libary OpenCV as cv2
import cv2

# defind a variable image keep a value calling a module cv2 function .imread()
# .imread() = reading an image and inside of function ('path of an image')
image = cv2.imread('imgs/images.jpeg')

# .imshow() = show an image or output
# .imshow() define with 2 parameter = 1. label program 2. image (.imread()) 
cv2.imshow('Image for output', image)

# .waitKey() = waiting program
# 0 it's means press any button for....
cv2.waitKey(0)
# close the program
cv2.destroyAllWindows()