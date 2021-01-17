# to prform AND between the sigma thresholded image that contains portions of ribcage and the ROI image in order to remove te ribcage

import os
import cv2
import numpy as np
from PIL import Image

folder_path = "C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/temp_patient_NewMask/"
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
		path_roi = str(os.path.join(image_path,image_list[2]))

		img = cv2.imread(path_image,0)
		img = img[100:380,150:380]
		roi =  cv2.imread(path_roi,0)

		img1 = Image.fromarray(img)
		roi1 = Image.fromarray(roi)

		print(img.shape)
		print(roi.shape)
		M1,N1 = img.shape
		M2,N2 = roi.shape

		# print(img.shape)
		# print(mask.shape)
		print("\n")
		print(M1,N1,M2,N2)
		print("\n")

		img2 = img1.resize((200,250))
		roi2 = roi1.resize((200,250))
		newimage = np.array(img2)
		newroi = np.array(roi2)
		print(newimage.shape)
		print(newroi.shape)
		

		sigmaANDroi = cv2.bitwise_and(newimage,newroi)
		cv2.imwrite(os.path.join(image_path,"sigma_AND_roi_{}".format(image_list[0])),sigmaANDroi)
		
