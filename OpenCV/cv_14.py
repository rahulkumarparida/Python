import cv2
import numpy as np
cap = cv2.VideoCapture('F:/Study/Python/OpenCV/vid1.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter('Output.mp4' , fourcc , 24.0 , (1280,720))

while cap.isOpened():
    ret , frame = cap.read()

    if ret:
        resized_frame = cv2.resize(frame, (1280, 720))

        output.write(resized_frame)
        cv2.imshow('frame' , resized_frame)

        if cv2.waitKey(10)== ord('s'):
            break
    else:
        break


cv2.destroyAllWindows()