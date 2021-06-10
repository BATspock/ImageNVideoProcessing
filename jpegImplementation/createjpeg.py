import cv2
import os
import numpy as np

def addBorderReplicateforJPEG8X8(im: np.ndarray) -> np.ndarray:

    assert (type(im) == np.ndarray)

    top , bottom, left, right = 0,0,0,0    
    rows, cols = im.shape[0], im.shape[1]

    if (rows%8):
        extra_r = 8-rows%8
        top,bottom = extra_r//2, (extra_r-extra_r//2)

    if (cols%8):
        extra_c = 8-cols%8
        left, right = extra_c//2, (extra_c-extra_c//2)

    im = cv2.copyMakeBorder(im, top, bottom, left, right, borderType= cv2.BORDER_REPLICATE )

    return im

img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

for img in os.listdir(img_pth)[:3]:
    
    im = addBorderReplicateforJPEG8X8(cv2.imread(img_pth+img, 0))     

    for r in range(0,im.shape[0], 8):
        for c in range(0,im.shape[1], 8):
            
            val = (1/64)*np.sum(im[r:r+8, c: c+8])
            im[r:r+8,c:c+8] = val

    cv2.imshow("check", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
