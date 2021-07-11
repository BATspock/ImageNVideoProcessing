import cv2
import numpy as np
import os 

os.chdir("..")
#print(os.getcwd())


img_pth = str(os.getcwd())+"//misc//"

#print(img_pth)
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)

    if event == cv2.EVENT_RBUTTONDOWN:
        print(x," ", y)


for im in os.listdir(img_pth)[:3]:

    i = cv2.imread(img_pth+str(im),0)
    cv2.imshow("image", i)
    cv2.setMouseCallback("image", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()