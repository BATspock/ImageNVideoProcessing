import os
import cv2
from createjpeg import return_compressed_image

img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

#i = cv2.imread(img_pth+ '4.1.01.tiff', 0)
#cv2.imshow('image', i)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
for im in os.listdir(img_pth):
    
    i = cv2.imread(img_pth+str(im),0)
    cv2.imshow("original image", i )
    dct, compressed_image = return_compressed_image(img_pth+str(im))
    cv2.imshow("DCT", dct)
    cv2.imshow("compressed image",compressed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()