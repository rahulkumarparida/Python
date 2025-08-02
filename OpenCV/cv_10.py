import cv2
import numpy as np

img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' ) 


h = 400
w= 450
dim = (w,h)

resize = cv2.resize(img,dim)

ksize = 5

blur = cv2.medianBlur(resize , ksize   )

cv2.imshow("blur" , blur)

cv2.waitKey(0)
cv2.destroyAllWindows()