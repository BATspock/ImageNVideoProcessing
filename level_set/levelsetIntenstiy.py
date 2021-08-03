import numpy as np
import os 
import scipy.ndimage
import scipy.signal
import matplotlib.pyplot as plt
from skimage import color, io

os.chdir("..")



n_iter = 100

def grad(x):
    return np.array(np.gradient(x))


def norm(x, axis=0):
    return np.sqrt(np.sum(np.square(x), axis=axis))


def stopping_fun(x):
    return 1. / (1. + norm(grad(x))**2)


def default_phi(x):
    # Initialize surface phi at the border (5px from the border) of the image
    # i.e. 1 outside the curve, and -1 inside the curve
    phi = np.ones(x.shape[:2])
    phi[5:-5, 5:-5] = -1.
    return phi


#img = io.imread('twoObj.bmp')
#img = color.rgb2gray(img)
#img = img - np.mean(img)

# Smooth the image to reduce noise and separation between noise and edge becomes clear
#img_smooth = scipy.ndimage.filters.gaussian_filter(img, sigma)

#F = stopping_fun(img_smooth)

img_pth = img_pth = str(os.getcwd())+"//misc//"

for img in os.listdir(img_pth)[:3]:
    #img_arr = cv2.imread(img_pth+img,0)
    #img_arr = (img_arr//val)*val
    #cv2.imshow("check", img_arr)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    img = io.imread(img_pth+img)
    img = color.rgb2gray(img)
    img = img - np.mean(img)
    img_smooth = scipy.ndimage.filters.gaussian_filter(img, sigma=1)
    F = stopping_fun(img_smooth)

    dt = 1.

    phi = default_phi(img_smooth)

    for i in range(n_iter):
        dphi = grad(phi)
        dphi_norm = norm(dphi)

        dphi_t = F * dphi_norm

        phi = phi + dt * dphi_t

