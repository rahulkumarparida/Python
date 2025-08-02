import cv2
import numpy as np

img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' ) 


h = 400
w= 450
dim = (w,h)

resize = cv2.resize(img,dim)

d = 6
sigmacolor = 100
sigmaspace = 100

bilateral = cv2.bilateralFilter(resize , d , sigmacolor , sigmaspace )

cv2.imshow("bilateral" , bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()