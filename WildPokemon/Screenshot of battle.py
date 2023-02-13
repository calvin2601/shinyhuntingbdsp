
import cv2 as cv
import numpy as np

img = cv.imread('sendOut.png')

upper_left = (1000, 600)
bottom_right = (1050, 650)
# Rectangle marker indicates region of interest (ROI)
r = cv.rectangle(img, upper_left, bottom_right, (100, 50, 200), 1)
# ROI assignment
ROI = img[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]
# print(ROI)
# print(cv.cvtColor(ROI,cv.COLOR_BGR2HSV))
# hsv_file= cv.cvtColor(ROI,cv.COLOR_BGR2HSV)
#np.savetxt('textBoxArrayWithRect.csv',hsv_file.reshape(hsv_file.shape[0],-1),delimiter=',')
cv.imshow("Display window", img)


k = cv.waitKey(0)