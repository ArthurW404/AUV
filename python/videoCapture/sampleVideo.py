import numpy as np
import cv2 as cv

def getBlue(img):
    hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # threshold the HSV image to only get blue colors
    mask = cv.inRange(hsvImg, lower_blue, upper_blue)
    
    # BITwise-AND mask and original image
    res = cv.bitwise_and(img,img, mask=mask)
    return res

def FAST(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #create fast detector object
    fast = cv.FastFeatureDetector_create()

    # Obtain key points using FAST
    keypoints = fast.detect(gray, None)
    # num_kpts = len(keypoints)
    # print(f"Number of keypoints Detected: {num_kpts}")
    # print(keypoints[0])
    # extract key points as list 
    # pts = cv.KeyPoint_convert(keypoints)
    # print(pts[0])

    # draw rich keypoints on input image
    image = cv.drawKeypoints(image, keypoints, outImage=None, color=[0, 0, 255],flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    image = cv.resize(image, (1400, 900))
    return image

if __name__ == "__main__":
    cap = cv.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        corners = FAST(frame)
        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting framef
        cv.imshow('frame',corners)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
