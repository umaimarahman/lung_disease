#Before segmentation I need to find the mask 

import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path 
import os

input_path = Path("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/heqpngs/result143.png")

img = cv2.imread(str(input_path),0)
M,N = img.shape
array = np.array(img)
for a in range(1,M):
	print(array[a])

ret,thTOZERO = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imwrite(os.path.join("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/","tozero_mask.png"),thTOZERO)

#img = cv2.medianBlur(img,5)

ret,th = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
print(ret)
cv2.imwrite(os.path.join("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/","adaptive_mask.png"),th)


#Adaptive Mean Thresholding
thmean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
     			cv2.THRESH_BINARY,11,2)

cv2.imwrite(os.path.join("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/","adaptivemean_mask.png"),thmean)

#Adaptive Gaussian Thresholding
thgaussian = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
     			cv2.THRESH_BINARY,11,2)

cv2.imwrite(os.path.join("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/","adaptivegaussian_mask.png"),thgaussian)

#Otsu's Thresholding
#Otsu Mask without the gaussian Blur and the Median bLur looks good
ret1, th1 = cv2.threshold(img,ret,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Otsu Threshold value : " + str(ret1))
cv2.imwrite(os.path.join("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/","otsu_mask.png"),th1)

#Otsu's Thresholding after gaussian Filtering

blur = cv2.GaussianBlur(img,(5,5),0)
ret2,th2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imwrite(os.path.join("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/","otsugaussian_mask.png"),th2)

plt.hist(th2)