#!/usr/bin/env python
import cv2  
import numpy as np 
import matplotlib.pyplot as plt

frame = cv2.imread("./DSC00088.JPG")
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_red = np.array([1,100,0])
upper_red = np.array([20,255,255])
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(frame,frame, mask = mask)
res_rgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

img_Guassian = cv2.GaussianBlur(res_rgb,(5,5),0)

plt.imshow(img_Guassian)
plt.show()



