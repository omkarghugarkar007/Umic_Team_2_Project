import numpy as np
import cv2
from matplotlib import pyplot as plt


def detector(img1,img2):
    img1 = cv2.resize(img1,(360,360)) 
    #img2 = cv2.resize(img2,(360,360)) 
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
    print(len(good_matches))
    if(len(good_matches)>10):
        #-- Draw matches
        #img_matches = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1]+img2.shape[1], 3), dtype=np.uint8)
        #cv2.drawMatches(img1, kp1, img2, kp2, good_matches, img_matches, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        #-- Show detected matches
        ret,thresh = cv2.threshold(img2,127,255,1)
        image, contours,h = cv2.findContours(thresh,1,2)
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
            if len(approx) == 3:
                cv2.drawContours(img2,[cnt],0,(0,255,0),3)
        #edges = cv2.Canny(img2,100,300)
        cv2.imshow('Refined', img2)
        cv2.waitKey(0)
        return 1

    else:
        return 0    



img1 = cv2.imread('cone1.png',0)
img2 = cv2.imread('cone.jpg',0)# Image obtained from the bot

detector(img1,img2)

