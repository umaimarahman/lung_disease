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

#Function to calculate the mean intensity usup(k) higher than u(k) of k-th slice
def mean_sup(M,N,f,output_path,image_name):
	sum_sup=0
	Rk = 0
	mean_intensity_k = mean_intensity(M,N,f)
	for i in range(0,M-1):
		for j in range(0,N-1):
			if f[i][j] > mean_intensity_k:
				sum_sup+=f[i][j]
				Rk+=1

	mean_sup = sum_sup/Rk

	#calculating the standard deviation
	std_sum=0
	pixel_diff = np.zeros((M,N))
	for i in range(0,M-1):
		for j in range(0,N-1):
			if f[i][j] > mean_sup:
				pixel_diff[i][j] = f[i][j] - mean_sup
				pixel_diff[i][j] = pixel_diff[i][j] **2
				std_sum+=pixel_diff[i][j]

	sigma = math.sqrt(std_sum/(Rk-1))
	#thresholding using the mean_sup and sigma value

	binsupf = np.zeros((M,N))

	for i in range(0,M-1):
		for j in range(0,N-1):
			binsupf[i][j] = int(f[i][j] > mean_sup+sigma)

	binsupf = binsupf.astype(int)
	binsupf = np.multiply(255,binsupf)
	np.set_printoptions(threshold = np.inf)

	#print(binsupf)		
			 
	binsup_img = Image.fromarray(binsupf)
	#binsup_img.save('binsupimg.png')
	#binsup_img.show()
	cv2.imwrite(os.path.join(output_path,'sigma_{}.png'.format(image_name)),binsupf)
	#os.path.join(output_path,'binsupimg_{}'.format(count)+'.png')
	return()


#Function to calculate the mean intensity u(k) of k-th slice
def mean_intensity(M,N,f):
	#Computing sum of all the pixels.
	sum_of_pixel = 0
	for i in range(0,M-1):
		for j in range(0,N-1):
			sum_of_pixel+=f[i][j]

	product = N*M
	mean_intensity = sum_of_pixel/product

	return(mean_intensity)

#the image is a binary mask having intensity values either 0(for black) or 255(for white)
folder_path = "C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/patient_NewMask/"
folder_list = os.listdir(folder_path)
patients = len(folder_list)

for i in range(patients):
	image_path = os.path.join(folder_path,folder_list[i])
	image_list = os.listdir(image_path)
	# print(image_list)
	size_of_list = len(image_list)
	# print(size_of_list)
	if(size_of_list!= 0):
		access_img = str(image_path)+"/"+str(image_list[0])
		print(access_img)
		img = cv2.imread(str(access_img),0)
		blur = cv2.GaussianBlur(img,(5,5),0)
		M,N = img.shape
	
		#f is the array of pixels
		f = np.array(blur)
		# print(image_name)
		np.set_printoptions(threshold = np.inf)
		print(f)	
		mean_sup(M,N,f,image_path,image_list[0])
	
