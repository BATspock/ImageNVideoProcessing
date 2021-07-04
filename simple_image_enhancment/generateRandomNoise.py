import cv2
import numpy as np 
import os
import random

from numpy.lib.function_base import insert

os.chdir("..")
print(os.getcwd())


img_pth = str(os.getcwd())+"//misc//"

#print(img_pth)

class GenerateNoise(object):
    def __init__(self, im: np.ndarray):
        
        assert(len(im.shape) == 2)
        self.im = im

    def SaltPepperNoise(self, percentage: float)->np.ndarray:

        percentage = percentage/100.0
        r,c = self.im.shape[0], self.im.shape[1]
        coordinates=set()
        image = self.im.copy()

        while ((len(coordinates)/(r*c)) < percentage):
            x = random.randint(0,r-1)
            y = random.randint(0,c-1)

            coordinates.add((x,y))
            
        for i,j in (list(coordinates)):
            image[i,j] = random.choice([0,255])

        return image
        

        




for im in os.listdir(img_pth)[:3]:
    i = cv2.imread(img_pth+str(im),0)
    noise = GenerateNoise(i)
    snp = noise.SaltPepperNoise(10)
    cv2.imshow("Salt and Pepper", snp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    



