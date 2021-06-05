import cv2
import os
import numpy as np
 
img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

avg_filter_kernel_3 = np.ones((3,3))
avg_filter_kernel_10 = np.ones((10,10))
avg_filter_kernel_20 = np.ones((20,20))



for img in os.listdir(img_pth):
    im = cv2.imread(img_pth+img, 0)
    im1 = cv2.filter2D(im, -1, avg_filter_kernel_3*(1/9))
    im2 = cv2.filter2D(im, -1, avg_filter_kernel_10*(1/100))
    im3 = cv2.filter2D(im, -1, avg_filter_kernel_20*(1/400))
    cv2.imshow('avg_3', im1)
    cv2.imshow('avg_10', im2)
    cv2.imshow('avg_20', im3)
    cv2.waitKey(0)

