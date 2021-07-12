from sys import modules
import cv2
import numpy as np
import os 
from sepration import create_fg

os.chdir("..")
#print(os.getcwd())


img_pth = str(os.getcwd())+"//misc//"

mouse_clicks=list()
#print(img_pth)
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, " ", y)

    mouse_clicks.append([x,y])

def foreground_create(image: np.ndarray, x: int, y: int, threshold: float)->np.ndarray:
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            dis = create_fg(mouse_clicks[0][0], mouse_clicks[0][1], r, c, image)
            if (dis<threshold):
                image[r,c] = 255

    return image.copy()


for im in os.listdir(img_pth)[:1]:

    i = cv2.imread(img_pth+str(im),0)
    cv2.imshow("image", i)
    cv2.setMouseCallback("image", click_event)
    #add code to show separated image
    cv2.waitKey(0)
    cv2.destroyAllWindows()