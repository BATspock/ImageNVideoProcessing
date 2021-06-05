import cv2
import os
import numpy as np
 
img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

avg = np.ones((3,3))
avg_5 = np.ones((5,5))

for img in os.listdir(img_pth)[:3]:
    im = cv2.imread(img_pth+img, 0)
    im3 = im.copy()
    im5 = im.copy()
    im7 = im.copy()

    for r in range(0,im.shape[0], 3):
        for c in range(0,im.shape[1], 3):
            val = (1/9)*np.sum(im[r:r+3, c: c+3])
            im3[r:r+3,c:c+3] = val
    cv2.imshow("check_3", im3)

    for r in range(0,im.shape[0], 5):
        for c in range(0,im.shape[1], 5):
            val = (1/25)*np.sum(im[r:r+5, c: c+5])
            im5[r:r+5,c:c+5] = val
    cv2.imshow("check_5", im5)

    for r in range(0,im.shape[0], 7):
        for c in range(0,im.shape[1], 7):
            val = (1/49)*np.sum(im[r:r+7, c: c+7])
            im7[r:r+7,c:c+7] = val
    cv2.imshow("check_7", im7)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
