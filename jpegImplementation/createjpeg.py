import cv2
import os
import numpy as np
from scipy.fftpack import dct, idct

ENV_SHAPE = 8

def addBorderReplicateforJPEG8X8(im: np.ndarray) -> np.ndarray:

    assert (type(im) == np.ndarray)

    top , bottom, left, right = 0,0,0,0    
    rows, cols = im.shape[0], im.shape[1]

    if (rows%ENV_SHAPE):
        extra_r = ENV_SHAPE-rows%ENV_SHAPE
        top,bottom = extra_r//2, (extra_r-extra_r//2)

    if (cols%ENV_SHAPE):
        extra_c = ENV_SHAPE-cols%ENV_SHAPE
        left, right = extra_c//2, (extra_c-extra_c//2)

    im = cv2.copyMakeBorder(im, top, bottom, left, right, borderType= cv2.BORDER_REPLICATE )

    return im

img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

for img in os.listdir(img_pth)[:3]:
    
    im = addBorderReplicateforJPEG8X8(cv2.imread(img_pth+img))  

    im = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)   

    for r in range(0,im.shape[0], ENV_SHAPE):
        for c in range(0,im.shape[1], ENV_SHAPE):
            
            temp_block = im[r:r+ENV_SHAPE, c: c+ENV_SHAPE] - 128
            
            im[r:r+ENV_SHAPE,c:c+ENV_SHAPE] = val


    cv2.imshow("check", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
