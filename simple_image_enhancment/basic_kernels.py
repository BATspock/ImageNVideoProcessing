import cv2
import os

os.chdir("..")
print(os.getcwd())


img_pth = str(os.getcwd())+"//misc//"

#print(img_pth)


for im in os.listdir(img_pth)[:3]:

    i = cv2.imread(img_pth+str(im),0)   
    hi = cv2.equalizeHist(i)
    avg = cv2.blur(i,(8,8))
    med = cv2.medianBlur(i, 9)
    cv2.imshow("Origina image", i)
    cv2.imshow("histogram equlization", hi)
    cv2.imshow("averaging", avg)
    cv2.imshow("median blur", med)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
