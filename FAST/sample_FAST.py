import cv2
import numpy as numpy

def get_colour_similarity (bgr, colour):
    """
    Input bgr, and see how similar it is to the input colour
    returns 1 if colour is same, and the lower the number, the less similar
    """
    diff = 0
    for i in range(0,3):
        diff += (bgr[i] - colour[i]) ** 2
    return 1 - diff ** (1/2) / (3 * 255 ** 2) ** (1/2)

image = cv2.imread('gate.jpg')
yellow = [0,255,255]
for i in image:
    for j in image:
        pass

print(image[0][0])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#create fast detector object
fast = cv2.FastFeatureDetector_create()

# Obtain key points using FAST
keypoints = fast.detect(gray, None)
num_kpts = len(keypoints)
print(f"Number of keypoints Detected: {num_kpts}")
print(keypoints[0])
# extract key points as list 
pts = cv2.KeyPoint_convert(keypoints)
print(pts[0])

# draw rich keypoints on input image
image = cv2.drawKeypoints(gray, [keypoints[i] for i in range(int(num_kpts/2 - num_kpts/4), int(num_kpts/2 + num_kpts/4))], outImage=None, color=[0, 0, 255],flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

image = cv2.resize(image, (1400, 900))
cv2.imwrite('FAST.jpg', image)
cv2.waitKey()
cv2.destroyAllWindows()