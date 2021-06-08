import cv2
import os
import numpy as np

img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

avg = np.ones((8,8))

for img in os.listdir(img_pth)[:3]:
    
    im = cv2.imread(img_pth+img, 0)

    for r in range(0,im.shape[0], 8):
        for c in range(0,im.shape[1], 8):
            val = (1/64)*np.sum(im[r:r+8, c: c+8])
            im[r:r+8,c:c+8] = val
    cv2.imshow("check", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
