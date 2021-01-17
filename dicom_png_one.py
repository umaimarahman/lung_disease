#Convert dicom files in a folder to jpg

import pydicom as dicom
import pandas as pd
import cv2
import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from pathlib import Path



# function to convert dicom file to png and save it
def dicom2png(dicom_list,output_path,fname):
	
	for i,dicom_files in enumerate(dicom_list,0):
		ds = dicom.read_file(str(dicom_files),force = True)
		#print(ds.PatientName,dicom_list[i],ds.SeriesDescription)
		#print(ds)
		fn,fext = os.path.splitext(fname[i])
		
		Series_Description = str(ds.SeriesDescription)
		
		if Series_Description == "ThorHR  5.0  B31f":
		#dicom files stored as pixel array in the variable dicom_image
			
			print(ds.PatientName,fn,ds.SeriesDescription)
			with open("patient.txt", "a") as text_file:
				text_file.write("\n"+str(ds.PatientName)+"\t"+ str(fn)+"\t"+str(ds.SeriesDescription)+"\n")
			ds.file_meta.TransferSyntaxUID = dicom.uid.ImplicitVRLittleEndian
			dicom_image = ds.pixel_array
		#if ds.SeriesDescription != "Patient Protocol" or ds.SeriesDescription != "Dose Report":
		#window_type = ds.SeriesDescription
		#if str(window_type) == "ThorHR  5.0  B31f":

		#write the pixel_array as a png file
			cv2.imwrite(os.path.join(output_path,("output_{}.png".format(fn))),dicom_image)

		#histogramequalization(image_index)
		#image_index = image_index + 1
	return


file_list = []
#path of the directory which contains sub-directories that in turn contains .dcm files
subfolder_path = Path("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/HRCT_IPCR/20180619/10270004")
file_list = os.listdir(subfolder_path)

#print(file_list)
#['10010000','10010001','10010002','10270000','10270001','10270002','10270003','10270004','10580000','10580001','10580002','10580003','10580004']

dicom_name_list = []
filename=[]
for dicom_files in file_list:
	file_path = subfolder_path/dicom_files
		#print("--------------------- FILE --------------------")
		#print(file_path)
		#file_path variable displays the path of each dicom file available
	dicom_name_list.append(file_path)
		#dicom_name_list is a list that contains the file_path of each dicom file
	filename.append(dicom_files)
# print("==========================Path of the first 5 dicom files :================================================\n ")
# print(dicom_name_list[:5])

print("*****************************************************Image name list********************************************************************")

#contains the path where the .jpg files will be stored
output_path = Path("data/pngs/newpng/")

dicom2png(dicom_name_list,output_path,filename)



		
	

