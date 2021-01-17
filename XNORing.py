#The idea is to take one image(mask) which is the last image that gives the shape of the heart and xnor it with all the other images and keep the rsultant
import cv2
import numpy as np
import os
from PIL import Image
import natsort

input_path1 = "data/pngs/roimasks/"
input_path2 =  "data/pngs/selectedroi/" 
output_path =  "data/pngs/selectedroi/" 
roi_list = os.listdir(input_path1)
XNORmask_list = os.listdir(input_path2)
roi_list = natsort.natsorted(roi_list,reverse = False)
XNORmask_list = natsort.natsorted(XNORmask_list,reverse = False)
imgarray = np.zeros((512,512))
selected = np.zeros((512,512))
for index, roi in enumerate(roi_list,0):
	imgarray = cv2.imread(os.path.join(input_path1,roi_list[index]))
	mask = cv2.imread(os.path.join(input_path2,XNORmask_list[0]))
	np.set_printoptions(threshold = np.inf)
	#print(imgarray)
	if index < 63:
		selected = cv2.bitwise_xor(imgarray,mask)
		cv2.imwrite(os.path.join(output_path,"selectedroi_{}.png".format(index)),selected)
	# if average > 52.0 and average < 55.0:
	# 	cv2.imwrite(os.path.join(output_path,"selectedroi_{}.png".format(index)),imgarray)
	# 	print("********   SElected :"+str(imgname)+"**********")
for index, image in enumerate(XNORmask_list):
	imgarray = cv2.imread(os.path.join(input_path2,XNORmask_list[index]),0)
	np.set_printoptions(threshold = np.inf)
	#print(imgarray)
	sum_of_bits = np.cumsum(imgarray)
	total_bits = imgarray.size
	average = sum_of_bits[-1]/total_bits
	imgname = np.array(image)
	print("==========================================================="+str(imgname)+"====================================================")
	#print(sum_of_bits[-1])
	print(average)