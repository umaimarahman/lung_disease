import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path 
import os
from PIL import Image
import math
import re
import natsort



input_path = Path("data/pngs/heqpngs/")
output_path = Path("data/pngs/patient_masks/selectedroi4/")
image_folder = os.listdir(input_path)

image_folder = natsort.natsorted(image_folder,reverse = False)

#P is the number of CT Scan slices

print(image_folder)

mask_folder = os.listdir(output_path)
mask_folder = natsort.natsorted(mask_folder,reverse = False)
print(mask_folder)
P = len(mask_folder)
print(mask_folder[0])

res_mask = np.zeros((512,512))
#to calculate the common area to all the P masks
img_mask1 = cv2.imread(os.path.join(output_path,mask_folder[0]),0)
img_mask2 = cv2.imread(os.path.join(output_path,mask_folder[1]),0)
res_mask = img_mask1 & img_mask2
cv2.imwrite(os.path.join(output_path,'maskImage.png'),res_mask)
for count,mask in enumerate(mask_folder,0):
	if(count<64):

		mask = cv2.imread(os.path.join(output_path,mask_folder[count]),0)
		res_mask = cv2.bitwise_and(res_mask,mask)
		count+=1


############################
np.set_printoptions(threshold = np.inf)
print(res_mask)

maskImage = Image.fromarray(res_mask)

#res_mask = cv2.bitwise_not(res_mask)

cv2.imwrite(os.path.join(output_path,'maskImage.png'),res_mask)
maskImage.show()



#morphological dilation : thickens white region
kernel = np.ones((8,5),np.uint8)
img =cv2.imread(os.path.join(output_path,"maskImage.png"),0)
dilation=cv2.dilate(img,kernel,iterations=1)
cv2.imwrite(os.path.join(output_path,"DilatedImage.png"),dilation)
cv2.imshow('dilation',dilation)
cv2.waitKey(0)

#dilation = cv2.bitwise_not(dilation)
cv2.imwrite(os.path.join(output_path,"DilatedImage.png"),dilation)

dilated_img = cv2.imread("data/pngs/patient_masks/selectedroi4/DilatedImage.png")
dil_img_negate = cv2.bitwise_not(dilated_img)

cv2.imwrite(os.path.join(output_path,"negationdilation.png"),dil_img_negate)
cv2.waitKey(0)


#morphological erosion : thins out the white regions
kernel = np.ones((8,5),np.uint8)
img =cv2.imread(os.path.join(output_path,"negationdilation.png"),0)
erosion = cv2.erode(img, kernel, iterations=1) 
cv2.imwrite(os.path.join(output_path,"ErodededImage.png"),erosion)
cv2.imshow('erosion',erosion)
cv2.waitKey(0)


