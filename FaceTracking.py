import cv2
import numpy as np

def findFace():
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgrey, 1.2, 8)
    myFacelistc = []
    myFacelistArea = []

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cx = x+w//2
        cy = y+h//2
        area = w*h
        cv2.circle(img, (cx,cy), 5, (0,255,0), cv2.FILLED)
        myFacelistc.append([cx, cy])
        myFacelistArea.append(area)
    if len(myFacelistArea) != 0:
        i = myFacelistArea.index(max(myFacelistArea))
        return img, [myFacelistArea[i],myFacelistc[i]]
    else:
        return  img, [[0,0], 0]


cap = cv2.VideoCapture()
while True:
    _, img = cap.read()
    img, info = findFace(img)
    print("Area", info[1])
    cv2.imshow("Output", img)
    cv2.waitKey(1)
