#!/usr/bin/env python3
import cv2
vid = cv2.VideoCapture(1)
while True:
    ret, frame = vid.read()
    cv2.imshow('Aimy Rpi4 usb camera', frame)   
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
