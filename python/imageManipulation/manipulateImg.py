import numpy
import cv2

image = cv2.imread("images/gate.jpg")

print(image[100,100])

# changing a portion of the image into black
image[0:500, 0:500] = (0, 0, 0)

# bluring image
# x * x pixels around a pixel is taken and the median of all the pixel values is used to relace that pixel
x = 21
# changing second parameter changes how much is blurred
image = cv2.medianBlur(image, x)

image = cv2.resize(image, (900, 600))

cv2.imshow("cool image", image)
cv2.waitKey(0)