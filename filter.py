# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:34:22 2018

@author: garcia
"""

import numpy as np
import cv2

def myfanc(i):
    pass #do nothing

cv2.namedWindow('title')
cv2.createTrackbar('sigmaColor','title',0,100,myfanc)
cv2.createTrackbar('sigmaSpace','title',0,100,myfanc)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)


while(True):
     ret, frame = cap.read()
     if not ret : continue
 
     w = cv2.getTrackbarPos('sigmaColor','title')
     x = cv2.getTrackbarPos('sigmaSpace','title')
     
     img = cv2.bilateralFilter(frame,9,w,x)
     cv2.imshow('title',img)
     k = cv2.waitKey(1)
     if k==ord('q')or k == 27:
         break

cap.release()
cv2.destroyAllWindows()