from sys import modules
import cv2
import numpy as np
import os 
from sepration import create_fg

os.chdir("..")
#print(os.getcwd())


img_pth = str(os.getcwd())+"//misc//"

#print(img_pth)
def click_event(event, x, y, flags, params):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        print("foreground pixel location: ",x, " ", y)

    mouseX, mouseY = x, y

def foreground_create(image: np.ndarray, x: int, y: int, threshold: float)->np.ndarray:
    print("foreground create")
    for r in range(image.shape[0]):
        for c in range(image.shape[1]):
            dis = create_fg(mouseX, mouseY, r, c, image)
            if (dis<threshold):
                image[r,c] = 255

    return image.copy()


image_list =  os.listdir(img_pth)
im = cv2.imread(img_pth+str(image_list[0]),0)
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_event)
cv2.imshow("image", im)



cv2.waitKey(0)
im_new = foreground_create(im, mouseX, mouseY, 5)
cv2.imshow("new image", im_new)
cv2.waitKey(0)
cv2.destroyAllWindows()
