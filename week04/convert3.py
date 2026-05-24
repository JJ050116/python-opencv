import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./imgs/superman.jpg')

# normal image
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# GrayScale 3 inch
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_3in = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

# finding a red color
# HSV = tone color
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# tone lower
# np.array() = storing the code RGB in Array
lower_red = np.array([0, 120, 70])
# tone higher
upper_red = np.array([10, 255, 255])
# .inRange() = range tone color btween lower and higher
mask = cv2.inRange(img_hsv, lower_red, upper_red)

# comparision btween color(normal) and color grayscale

# .bitwise_and() = comparision 2 things
color_part = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)
gray_part = cv2.bitwise_and(gray_3in, gray_3in, mask=cv2.bitwise_not(mask))

# merge btween normal image and gray scale
final_image = cv2.add(color_part, gray_part)

# showing the image final after merge
plt.imshow(final_image)
# create a title
plt.title('Color Splash: Red ONLY!!')
# showing the output
plt.show()