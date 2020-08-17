import numpy as np
import cv2
from matplotlib import pyplot as plt
from pyimagesearch.shapedetector import ShapeDetector

def detector(img1,img2_color):
    img1 = cv2.resize(img1,(360,360)) 
    img2 = cv2.cvtColor(img2_color,cv2.COLOR_BGR2GRAY)
    #img2 = cv2.resize(img2,(500,360)) 
    #img2_color = cv2.resize(img2_color,(500,360)) 
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1,None)
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 10)
    search_params = dict(checks = 50)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    kp2, des2 = sift.detectAndCompute(img2,None)
    matches = flann.knnMatch(des1,des2,k=2)
    ratio_thresh = 0.8
    good_matches = []
    for m,n in matches:
        if m.distance < ratio_thresh * n.distance:
            good_matches.append(m)
    list_kp2 = [kp2[mat.queryIdx].pt for mat in good_matches] 
    pts = [[i[0],i[1]] for i in list_kp2]
    print(list_kp2)
    x = np.mean([pts[i][0] for i in range(len(pts))])
    y = np.mean([pts[i][1] for i in range(len(pts))])
    if(len(good_matches)>5):   
        cv2.ellipse(img2_color,(int(x),int(y)),(100,100),0,0,360,(0,255,0),4)    
        cv2.imshow('Refined', img2_color)
        cv2.waitKey(0)
        return 1
    else:
        return 0    



img1 = cv2.imread('cone.jpg',0)
img2 = cv2.imread('cone1.png')# Image obtained from the bot

detector(img1,img2)

