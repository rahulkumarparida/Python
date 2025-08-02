import cv2

img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' , 1)

print("Dimesion : ", img.shape)

scale = 150
w = int(img.shape[1]*scale / 100)
h = int(img.shape[0]*scale / 100)

dim = (w,h)

resized = cv2.resize(img , dim , interpolation=cv2.INTER_AREA)

print("Dimesion : ", resized.shape)

cv2.imshow("resize" , resized)
cv2.imshow('Og', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


