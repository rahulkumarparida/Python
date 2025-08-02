import cv2
import numpy as np

img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' ,0) 
h = 400
w= 450
dim = (w,h)
resize = cv2.resize(img,dim)

min_thresh = 100
max_thresh = 200

edge = cv2.Canny(resize , min_thresh , max_thresh ,)



cv2.imshow("edge" , edge)

cv2.waitKey(0)
cv2.destroyAllWindows()