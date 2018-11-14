#this code shall run on the laptop
# Message Sender
import os
from socket import *
import cv2
import numpy as np
host = "192.168.43.46" # set to IP address of target computer....this is the IP of my RaspberryPi
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

eye_cascade=cv2.CascadeClassifier('parojosG.xml')

cap=cv2.VideoCapture(0)
#cap1=cv2.VideoCapture(1)
direction=b'forward'
cnt=0
roi_gray=cv2.imread('randompic2.jpg')
kernel=np.ones((4,4),np.uint8)
resize=cv2.imread('randompic2.jpg')
while 1:
    ret,img=cap.read()
    #ret1,im1=cap1.read()
    #cv2.imshow('WebcamVideo',im1)
    #cv2.imshow('LaptopVideo',img)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    eyes=eye_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in eyes:
        w=int(w/2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        
        roi_gray=cv2.adaptiveThreshold(roi_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
        roi=img[y:y+h,x:x+w]
        resize = cv2.resize(roi,(640, 480))
        h1=int(h/2) +1
        w1=int(w/4) +4
        w2=int(w1*3) -17
        #roi_gray[0:h1,0:w1]=0
        #roi_gray[h1:h,w2:w]=0
        pt1=roi_gray[h1,w1]
        pt2=roi_gray[h1,w2]
        if(pt1==0):
            direction=b'right'
        elif(pt2==0):
            direction=b'left'
        else:
            direction=b'forward'
    #roi_gray=cv2.morphologyEx(roi_gray,cv2.MORPH_OPEN,kernel)
    
    
    cv2.imshow('eye_resized',resize)
    cv2.imshow('eye',roi_gray)
    if(cnt==10):
        print(direction)
        UDPSock.sendto(direction, addr)
        cnt=0
    cnt+=1
    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
UDPSock.close()
os._exit(0) 
        


    
    

