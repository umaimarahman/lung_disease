#calculating the global mean uglobal
# global mean = mean of the usup(k) - std dev of usup(k)
#global mean is computed using the entire CT Scan

import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path 
import os
from PIL import Image
import math

#Function to calculate the mean intensity usup(k) higher than u(k) of k-th slice
def mean_sup(M,N,f):
	sum_sup=0
	Rk = 0
	mean_intensity_k = mean_intensity(M,N,f)
	for i in range(0,M-1):
		for j in range(0,N-1):
			if f[i][j] > mean_intensity_k:
				sum_sup+=f[i][j]
				Rk+=1

	mean_sup = sum_sup/Rk
	return(mean_sup)


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
input_path = Path("data/pngs/heqpngs/")

image_folder = os.listdir(input_path)

#P is the number of CT Scan slices
P = len(image_folder)
#print(image_folder)

mean_sup_intensity_k = []
#iterate over each image and find its 
for k_image in image_folder:
	img = cv2.imread(os.path.join(input_path,k_image),0)
	
	M,N = img.shape

	#f is the aray of pixels
	f = np.array(img)

	np.set_printoptions(threshold = np.inf)

	#calculating the mean_sup of each slice
	mean_sup_intensity_k.append(mean_sup(M,N,f))

#print(mean_sup_intensity_k)

#calculating the mean of musup(k)
mean_meansup = sum(mean_sup_intensity_k)/P

#calculating the standard deviation of musup(k)
first_term = sum(mean_sup_intensity_k)/(P-1)
sq_sum=0
for k in range(0,P-1):
	sq_sum+=mean_sup_intensity_k[k] **2

second_term = sq_sum/P

sqrt_term = math.sqrt(abs(first_term-second_term))


global_mean = mean_meansup - sqrt_term

print("Global mean : " + str(global_mean))

# Thresholding he image using global mean

#testing thresholding only on one picture

input_path = Path("data/pngs/heqpngs/result32.png")
img = cv2.imread(str(input_path),0)
blur = cv2.GaussianBlur(img,(5,5),0)
M,N = img.shape
print(M,N)
#f is the aray of pixels
f = np.array(blur)

#thresholding using the global mean value000000000000000000
binglobalf = np.zeros((M,N))
for i in range(0,M-1):
	for j in range(0,N-1):
		
		binglobalf[i][j] = int(f[i][j] > global_mean)

binglobalf = binglobalf.astype(int)
binglobalf = np.multiply(255,binglobalf)

np.set_printoptions(threshold = np.inf)

print(binglobalf)		
			 
bin_img = Image.fromarray(binglobalf)

bin_img.save('binimg.png')
bin_img.show()

