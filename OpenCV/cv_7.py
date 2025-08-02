import cv2
import numpy as np

img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' ) 

row = img.shape[1]
col = img.shape[0]

center = ( col/2,row/2)
angle = 90

r=cv2.getRotationMatrix2D(center , angle ,1)

rotate =cv2.warpAffine(img , r,(col ,row))

cv2.imshow("Rotate",rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
