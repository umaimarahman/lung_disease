#and the negative of morphological dilation with the roi masks

import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path 
import os
from PIL import Image
import natsort



input_path = Path("data/pngs/patient_masks/selectedroi4/")
spineless_path = Path("data/pngs/patient_masks/spineless4/")
aorta_path = Path("data/pngs/patient_masks/aorta_p4/")
AND_img = cv2.imread(os.path.join(input_path,"spine.png"),0)
image_folder = os.listdir(input_path)
image_folder = natsort.natsorted(image_folder,reverse = False)

for i, image in enumerate(image_folder,0):
	im = cv2.imread(os.path.join(input_path,image_folder[i]),0)
	M,N = im.shape
	spineless = cv2.bitwise_and(AND_img,im)
	spineless = spineless[20:200,0:300]
	blur = cv2.GaussianBlur(spineless,(5,5),0)
	cv2.imwrite(os.path.join(spineless_path,"spineless4_{}.png".format(i)),spineless)

img_without_spine = cv2.imread(os.path.join(spineless_path,"spineless4_12.png"),0)
img_aorta = cv2.imread(os.path.join(aorta_path,"aorta_6.png"),0)
complete_img = np.zeros((M,N))
complete_img = cv2.bitwise_or(img_without_spine,img_aorta)

cv2.imwrite(os.path.join(aorta_path,"Complete_mask.png"),complete_img)
