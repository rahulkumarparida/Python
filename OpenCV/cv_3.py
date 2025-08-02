import cv2

img =cv2.imread('F:/Study/Python/OpenCV/2.jpg' , 1)

h = 400
w= 450
dim = (w,h)

resize = cv2.resize(img,dim)

cv2.imshow("resized" , resize)

flip = cv2.flip(resize,-1)

cv2.imshow("Flipped" , flip)
print(flip.size , "<--flipped size , originals size-->", resize.size)
cv2.waitKey(0)
cv2.destroyAllWindows()
