#compute the P masks by thresholding with usup(k) an store it in the foldr /maskpng

import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path 
import os
from PIL import Image
import math
import re
import natsort


#Function to calculate the mean intensity u(k) of k-th slice
def mean_intensity(M,N,f,count,output_path):
	#Computing sum of all the pixels.
	sum_of_pixel = 0
	for i in range(0,M-1):
		for j in range(0,N-1):
			sum_of_pixel+=f[i][j]

	product = N*M
	mean_intensity = sum_of_pixel/product
	#thresholding using the mean value

	binf = np.zeros((M,N))

	for i in range(0,M-1):
		for j in range(0,N-1):
			binf[i][j] = int(f[i][j] > mean_intensity)

	binf = binf.astype(int)
	binf = np.multiply(255,binf)

	np.set_printoptions(threshold = np.inf)

	print(binf)		
				 
	bin_img = Image.fromarray(binf)
	cv2.imwrite(os.path.join(output_path,'binimg_{}.png'.format(count)),binf)

	return()

#the image is a binary mask having intensity values either 0(for black) or 255(for white)
input_path = Path("data/pngs/heqpngs/")
output_path = Path("data/pngs/maskpngs")
image_folder = os.listdir(input_path)

image_folder = natsort.natsorted(image_folder,reverse = False)

#P is the number of CT Scan slices
P = len(image_folder)
print(image_folder)
count = 0
for k_image in image_folder:
	img = cv2.imread(os.path.join(input_path,k_image),0)
	blur = cv2.GaussianBlur(img,(5,5),0)
	M,N = img.shape

	#f is the aray of pixels
	f = np.array(blur)

	np.set_printoptions(threshold = np.inf)
	
	mean_intensity(M,N,f,count,output_path)
	count+=1
	#print(count)
print("Bye")
