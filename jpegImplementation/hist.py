import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

def create_histogram(im :np.ndarray, channel = 0, mask = None)->np.ndarray:
    
    return cv2.calcHist([im],[channel],mask,[256],[0,256])


os.chdir("..")
print(os.getcwd())


img_pth = str(os.getcwd())+"//misc//"

#i = cv2.imread(img_pth+ '4.1.01.tiff', 0)
#cv2.imshow('image', i)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
for im in os.listdir(img_pth)[:3]:
    i = cv2.imread(img_pth+str(im), 0)
    hist = create_histogram(i)
    plt.plot(hist)
    plt.show()

