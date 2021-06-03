import cv2
import os
import numpy as np
import math 

img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

print("max intensity of image is 256")

intensity = int(input("Enter intensity level by which to reduce image (must be an integer in the range of 0 to 8): "))

assert intensity>=0 and intensity<=8

val = 2**intensity;

for img in os.listdir(img_pth):
    img_arr = cv2.imread(img_pth+img,0)
    img_arr = (img_arr//val)*val
    cv2.imshow("check", img_arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    