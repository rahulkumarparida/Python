import cv2

img = cv2.imread('F:/Study/Python/OpenCV/2.jpg',0)


# cv2.imwrite('highway.jpg', img) # To write and save the image

width = img.shape[1]
height = 300
dimen = (width , height)
resized = cv2.resize(img , dimen)

 
cv2.imshow('image-reader' , resized)        

cv2.waitKey(0)
print(resized.shape)   
cv2.destroyAllWindows()