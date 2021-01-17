import cv2
import numpy as np
import os
from PIL import Image
import natsort

input_path = "C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/patient_masks/patient4/"
output_path =  "C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/patient_masks/selectedroi4/" 
image_list = os.listdir(input_path)
image_list = natsort.natsorted(image_list,reverse = False)
imgarray = np.zeros((512,512))

for index, image in enumerate(image_list,0):
	imgarray = cv2.imread(os.path.join(input_path,image_list[index]),0)
	#imgarray = imgarray[110:350,150:350]
	#cv2.imwrite(os.path.join(input_path,"p4_mask{}.png".format(index)),imgarray)
	np.set_printoptions(threshold = np.inf)
	#print(imgarray)
	img_crop1 = imgarray[:150,150:]
	img_crop2 = imgarray[200:,:150]
	sum_of_crop1= np.cumsum(img_crop1)
	sum_of_crop2= np.cumsum(img_crop2)
	average1 = round(sum_of_crop1[-1]/img_crop1.size)
	average2 = round(sum_of_crop2[-1]/img_crop2.size)
	imgname = np.array(image)
	sum_of_bits = np.cumsum(imgarray)
	average = round(sum_of_bits[-1]/imgarray.size)
	print("==========================================================="+str(imgname)+"====================================================")
	#print(sum_of_bits[-1])
	print("Average1 : \t"+str(average1)+"\t Average2 : \t"+str(average2) +"\t Average sum : \t"+str(average))

	# #if average1 > 20.0 and average1 < 50.0 and average2 > 70.0 and average2 < 90.0 and average < 90.0:
	if average > 50.0 and average <90.0:
		cv2.imwrite(os.path.join(output_path,"selectedroi_{}.png".format(index)),imgarray)
		print("********   Selected :"+str(imgname)+"**********")
