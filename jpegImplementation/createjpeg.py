import cv2
import os
import numpy as np
from scipy.fftpack import dct, idct

QUANTIZATION_MATRIX = np.array([[16,11, 10, 16,24,40,51,61],
                                  [12,12,14,19,26,58,60,55],
                                  [14,13,16,24,40,57,69,56],
                                  [14,17,22,29,51,87,80,62],
                                  [18,22,37,56,68,109,103,77],
                                  [24,35,55,64,81,104,113,92],
                                  [49,64,78,87,103,121,120,101],
                                  [72,92,95,98,112,100,103,99]])

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

def apply_dct(a):
    test_image = np.zeros((im.shape[0], im.shape[1]))
    test_image = dct(dct(a.T, norm='ortho').T, norm='ortho')
    return test_image

def apply_idct2(a):
    test_image = np.zeros((im.shape[0], im.shape[1]))
    test_image =  idct(idct(a.copy().T, norm='ortho').T, norm='ortho') 
    return test_image

def applyDCTonImage(im, ENV_SHAPE= 8) -> np.ndarray:
    test_image = np.zeros((im.shape[0], im.shape[1]));

    for r in range(0,im.shape[0], ENV_SHAPE):
        for c in range(0,im.shape[1], ENV_SHAPE):
            
            temp_block = im[r:r+ENV_SHAPE, c: c+ENV_SHAPE] - 128
            dct_temp_block = apply_dct(np.int64(temp_block))
            dct_temp_block = qunatize_dct_8x8(dct_temp_block)
            test_image[r:r+ENV_SHAPE, c: c+ENV_SHAPE] = dct_temp_block
    return test_image


def applyIDCTonImage(im, ENV_SHAPE= 8) -> np.ndarray:
    
    test_image = np.zeros((im.shape[0], im.shape[1]));

    for r in range(0,im.shape[0], ENV_SHAPE):
        for c in range(0,im.shape[1], ENV_SHAPE):
            
            temp_block = im[r:r+ENV_SHAPE, c: c+ENV_SHAPE] 
            temp_block = return_qunatize_8x8_for_idct(temp_block)
            idct_temp_block = apply_idct2(temp_block)
            test_image[r:r+ENV_SHAPE, c: c+ENV_SHAPE] = idct_temp_block + 128
    return test_image

def qunatize_dct_8x8(im : np.ndarray,  q = QUANTIZATION_MATRIX) -> np.ndarray:
    return np.int64(np.true_divide(im, q))


def return_qunatize_8x8_for_idct(im :np.ndarray, q = QUANTIZATION_MATRIX) -> np.ndarray:
    return np.multiply(im,q)



img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

for img in os.listdir(img_pth)[:]:
    
    im = addBorderReplicateforJPEG8X8(cv2.imread(img_pth+img,0))
    #print(im.dtype)
    cv2.imshow("check", im)  
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2YCR_CB)  
    #print(im[0:8,0:8])
    get_DCT_image = applyDCTonImage(im.copy())    
    #print(get_DCT_image.dtype)
    #print(get_DCT_image[0:8,0:8])
    cv2.imshow("check_DCT", get_DCT_image)
    get_IDCT_image = applyIDCTonImage(get_DCT_image.copy())
    #get_IDCT_image = np.asarray(get_IDCT_image, dtype=np.float64)
    #cv2.imshow("check_idct", get_IDCT_image)
    #print(get_IDCT_image.dtype)
    #print(get_IDCT_image[0:8,0:8])
    get_IDCT_image = np.uint8(get_IDCT_image)
    #print(get_IDCT_image[0:8,0:8])
    cv2.imshow("check_idct_uint8", get_IDCT_image)
    #print(np.allclose(get_IDCT_image,im) )
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
