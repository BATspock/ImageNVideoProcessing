import cv2
import os
import imutils

img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

rot = input("Enter the angle by which to rotate the image in degrees: ")

#rot = float(rot)
#for img in os.listdir(img_pth):
#    im = cv2.imread(img_pth+img, 0)
#    rot = imutils.rotate(im, 45)
#    cv2.imshow("check ", rot)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()  

for img in os.listdir(img_pth):
    im = cv2.imread(img_pth+img, 0)
    M = cv2.getRotationMatrix2D((im.shape[0]//2, im.shape[1]//2), float(rot), 1)
    i = cv2.warpAffine(im, M, (im.shape[1], im.shape[0]))
    cv2.imshow("rotation", i)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 