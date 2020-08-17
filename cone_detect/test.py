import numpy as np
import cv2
from matplotlib import pyplot as plt
from pyimagesearch.shapedetector import ShapeDetector

def detector(img1,img2_color):
    img1 = cv2.resize(img1,(360,360)) 
    img2 = cv2.cvtColor(img2_color,cv2.COLOR_BGR2GRAY)
    #img2 = cv2.resize(img2,(360,360)
    ret,thresh = cv2.threshold(img2,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    sd = ShapeDetector()
    cnts = []
    for cnt in contours:
        if sd.detect(cnt) == "triangle":
            cnts.append(cnt)
    cv2.drawContours(img2_color, contours, -1, (0,255,0), 3)        
    cv2.imshow('Refined', img2_color)
    cv2.waitKey(0)
    return None


img1 = cv2.imread('cone.jpg',0)
img2 = cv2.imread('cone1.png')# Image obtained from the bot

detector(img1,img2)

