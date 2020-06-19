import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

def getBlue(img):
    hsvImg = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # threshold the HSV image to only get blue colors
    mask = cv.inRange(hsvImg, lower_blue, upper_blue)
    
    # BITwise-AND mask and original image
    res = cv.bitwise_and(img,img, mask=mask)
    return res


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    blue = getBlue(frame)
    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the resulting framef
    cv.imshow('frame',blue)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
