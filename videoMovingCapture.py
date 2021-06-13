# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:28:03 2021

@author: jm980
"""
import cv2 as cv
import numpy as np
import datetime



#동적인 물체가 없으면 캡쳐본을 남기는 프로그램
cap = cv.VideoCapture('360_0273_Stitch_XHC.mp4')
bgs = cv.createBackgroundSubtractorKNN(dist2Threshold =500,detectShadows=False)

while cap.isOpened():
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame = cv.resize(frame,None,fx=0.3,fy=0.3,interpolation = cv.INTER_CUBIC)
    fgmask = bgs.apply(frame)
   
    
    cv.imshow('video', frame)
    #B&W 영상 추출
    cv.imshow('moving', fgmask)
    #cv.imshow('fm', fmask)
    
    blur = cv.blur(fgmask,(10,10))
    #cv.imshow('blured' , blur)
    
    verticalStructure = cv.getStructuringElement(cv.MORPH_ELLIPSE,(6, 6))
    #img = cv.erode(blur, verticalStructure)
    img = cv.dilate(blur, verticalStructure)
    
    
    img[img > 180] = 255
    img[img <= 180] = 0
    
    cv.imshow("imgToFindContours" , img)
    
    contours, hirachy = cv.findContours(img, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)
    print("contours : " + str(len(contours)))

    if len(contours) < 1 :
        saved = cv.imwrite( now + ".jpg" , frame)
    
    if cv.waitKey(1) == ord('q'):
        break
    
    
cap.release()
cv.destroyAllWindows()