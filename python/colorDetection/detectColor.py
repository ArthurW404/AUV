import cv2 as cv
import numpy as np

img = cv.imread("../images/buckets.jpg")

hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_not_red = np.array([10,0,0])
upper_not_red = np.array([150,99,99])


# threshold the HSV image to only get blue colors
mask = cv.inRange(hsvImg, lower_not_red, upper_not_red)


cv.imshow('img', img)
cv.imwrite('mask.jpg',mask)
cv.waitKey(0)
cv.destroyAllWindows()
