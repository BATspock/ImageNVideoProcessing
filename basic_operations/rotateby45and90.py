import cv2
import os
import imutils

img_pth = "C://Users//adkishor//Desktop//ImageNVideoProcessing//misc//"

rot = input("Enter the angle by which to rotate the image in degrees: ")

rot = float(rot)
for img in os.listdir(img_pth)[:2]:
    im = cv2.imread(img_pth+img, 0)
    rot = imutils.rotate(im, rot)
    cv2.imshow("check ", rot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  