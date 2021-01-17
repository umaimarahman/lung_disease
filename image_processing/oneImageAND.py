import os
import cv2
import numpy as np
from PIL import Image

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
		path_image = str(os.path.join(image_path,image_list[0]))
		path_mask = str(os.path.join(image_path,image_list[1]))

		img = cv2.imread(path_image,0)
		mask =  cv2.imread(path_mask,0)

		img1 = Image.fromarray(img)
		mask1 = Image.fromarray(mask)

		print(img.shape)
		print(mask.shape)
		M1,N1 = img.shape
		M2,N2 = mask.shape

		print(img.shape)
		print(mask.shape)
		resultant = cv2.bitwise_and(img,mask)
		cv2.imwrite(os.path.join(image_path,"AND_result{}.png".format(image_list[0])),resultant)
		

# listOfPlaces = ["Berlin", "Paris", "Lausanne"]  
# currentCity = "Lausanne"

# for i,place in enumerate(listOfPlaces):  
#     print ("comparing %s with %s: %s %d" % (place, currentCity, place == currentCity,i))