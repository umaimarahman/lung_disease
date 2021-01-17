import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import os
from pathlib import Path
import natsort

image_index = 0

imagelist = os.listdir("data/pngs/newpng/")
imagelist = natsort.natsorted(imagelist,reverse = False)

for i,image in enumerate(imagelist,0):
	
	input_path = Path("data/pngs/newpng/")
	output_path = Path("data/pngs/equalizedpngs/")
	if image.endswith(".png"):
		imagepath = os.path.join(input_path,imagelist[i])
		fn,fext = os.path.splitext(image)
		print(fn)
		img1 = cv2.imread(str(imagepath),0)
		equ = cv2.equalizeHist(img1)
		cv2.imwrite(os.path.join(output_path,("eq_{}.png".format(fn))),equ)
		image_index = image_index + 1







