
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path 
import os
from PIL import Image
import natsort

def automatic_roi(img):

	M,N = img.shape
	wmean = round(0.1 *N)
	wmax = round(0.3*N)


	array = np.array(img)
	w = array
	#to successfully print the numpy aray
	np.set_printoptions(threshold = np.inf)

	#print(array)



	for i in range(0,M-1):
		start = 0
		end = M
		for j in range(0,N-1):

			if w[j][i] == 0 and w[j+1][i] == 255:
				start = j
				break

		for j in range(start+1,N-1):
			if w[j][i] == 255 and w[j+1][i] == 0:
				end = j
				break

		wj = end - start
			
		if wj < wmax:
			for r in range(start,end):
				w[r][i] = 0
			wmean = wj
			wmax = end
			prevend = end
			
		elif wj > wmax:
			for r in range(0,prevend):
				w[r][i] = 0

	#print(prevend)
	#print(w)



	print(np.array_equal(array,w))

	img = Image.fromarray(w)

	roi = w[100:350,150:350]

	return roi



input_path = Path("data/pngs/sigmamaskpngs/")
output_path = Path("data/pngs/roimasks/")
image_folder = os.listdir(input_path)
image_folder = natsort.natsorted(image_folder,reverse = False)
print(image_folder)

for index,image in enumerate(image_folder,0):

	img = cv2.imread((os.path.join(input_path,image_folder[index])),0)
	ROI = automatic_roi(img)
	#roiImg = Image.fromarray(ROI)
	cv2.imwrite(os.path.join(output_path,"roi_{}.png".format(index)),ROI)

