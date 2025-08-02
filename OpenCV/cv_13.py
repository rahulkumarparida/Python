import cv2

cap = cv2.VideoCapture('F:/Study/Python/OpenCV/vid1.mp4')

h = 400
w = 450
dim = (w, h)

while cap.isOpened():
    _, frame = cap.read()
    


    resize = cv2.resize(frame, dim)

    cv2.imshow("vid", resize)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
