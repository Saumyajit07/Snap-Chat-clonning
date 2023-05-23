import cvzone
from cv2 import cv2
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv2.imread('star.png', cv2.IMREAD_UNCHANGED)
while True:
    _, frame = cap.read()
    grey_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(grey_scale)
    for(x, y, w, h) in faces:
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.5)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x-45, y-75])
    cv2.imshow('Snap Dude', frame)
    if cv2.waitKey(10) == ord('q'):
        break
