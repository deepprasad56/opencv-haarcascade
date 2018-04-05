


import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')


cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        smile = smile_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize =(55, 55), flags = cv2.CASCADE_SCALE_IMAGE)
    
        for (ex,ey,ew,eh) in smile:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'Smile',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
    



    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
