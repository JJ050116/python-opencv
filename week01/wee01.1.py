import cv2

# function = myFunction()

image = cv2.imread('imgs/images.jpeg')

# save an image
# .imwrite() includeing with 2 parameter 1. new name of file 2. image
save_image = cv2.imwrite('new2.jpeg', image)

# create a variable for reading a new file image
newFile = cv2.imread('new2.jpeg')

cv2.imshow('test', newFile)
cv2.waitKey(0)
cv2.destroyAllWindows()