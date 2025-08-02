import cv2
import numpy as np

# img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' , cv2.IMREAD_COLOR)
img = np.zeros(shape=[700,950,3],dtype='uint8')

cv2.line(img ,(0,0),(150,150),(255,0,0),2)


cv2.rectangle(img ,(200,150),(250,300),(0,255,0),3)


cv2.circle(img , (150,250),60,(0,0,255),4)


points = np.array([[100,50],[150,150],[250,300],[400,550],[550,600]] , np.int32)

cv2.polylines(img , [points] , True , (0,0,0),5)


font = cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(img , "This is CV" , (100,150),font,4 ,(255,255,255),8,cv2.LINE_AA)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

