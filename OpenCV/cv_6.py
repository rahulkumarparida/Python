import cv2
import numpy as np

img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' ) 

col = img.shape[1]
row = img.shape[0]

s = np.float32([(1,0,150),(0,1,70)]) 

shifted = cv2.warpAffine(img , s , (col, row))

cv2.imshow("OG" , img)
cv2.imshow('Shift', shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()