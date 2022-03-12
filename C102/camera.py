from tkinter import Frame
import cv2
VideoCaptureObject=cv2.VideoCapture(0)
ret,frame=VideoCaptureObject.read()
cv2.imwrite('photo.png',frame)
VideoCaptureObject.release()
cv2.destroyAllWindows()