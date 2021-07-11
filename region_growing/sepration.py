import cv2
import numpy as np
import os

from numpy.lib.type_check import imag 

def pixel_wt (px :int, py:int, image :np.ndarray)-> float:
    rows, cols = image.shape[0], image.shape[1]
    left, right, top, bottom, diag_bt, diag_top, o_dia_bt, o_dia_top = 0,0,0,0,0,0,0,0

    if (px>=1): left = image[px, py]
    if (px<= rows-2): right = image[px+1,py]

    if(py>=1): top = image[px, py-1]
    if(py<=cols-2) : bottom = image[px, py+1]

    if (px>=1 and py >=1): diag_top = image[px-1, py-1]
    if (px<=rows-2 and py<=cols-2) : diag_bt = image[px+1, py+1]

    if (px<=rows-2 and py >=1): o_dia_top = image[px+1, py-1]
    if (px >=1 and py <=rows-2): o_dia_bt = image[px-1, py+1]

    return (left+right+top+bottom+diag_bt+diag_top+o_dia_bt+o_dia_top+(2*image[px,py]))/9.0

def distance(wt :float, px :int, py :int, image :np.ndarray)-> float:
    
    p_wt = pixel_wt(px, py, image)
    return ((wt-p_wt)*(wt-p_wt))**(0.5)

def create_fg(x : int,y: int, px :int, py:int, image :np.ndarray)->np.ndarray:

    fg_wt = pixel_wt(x,y,image)
    pixel_distance = distance(fg_wt, px, py, image)

    return pixel_distance