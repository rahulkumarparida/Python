import cv2
import numpy as np

img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' ) 

threshold_value = 200
_,thresh = cv2.threshold(img , threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow('Og', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()