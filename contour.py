import numpy as np
import cv2
import natsort
import os

path = "data/pngs/patient_masks/selectedroi4/"
im = cv2.imread(os.path.join(path,"DilatedImage.png"))

H, W, channels =im.shape
blurred = cv2.pyrMeanShiftFiltering(im, 31, 91)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im, contours, -1, (0,0, 255), 2)

cv2.imwrite('out{}.jpg', im)
listlen = len(contours)
print(listlen)
area=[]
#area stores the area of each object
for i in range(listlen):
	area.append(cv2.contourArea(contours[i]))

print("Area of objects : \n"+str(area)+"\n")
objects = []
for i in range(listlen):
	if area[i] > 1000.0 and area[i] < 5000.0:
#max_area = max(area)
#if area[i] == max_area:
		cnt = contours[i]
		cv2.drawContours(im, [cnt], 0, (0,255,0), 0)
		cv2.imshow('image',im)
		print(area[i])
		cv2.waitKey(0)
		cv2.destroyAllWindows()
		objects.append(area[i])
		idx = i  # The index of the contour that surrounds your object
		mask = np.zeros_like(threshold)# Create mask where white is what we want, black otherwise
		cv2.drawContours(mask, contours, idx, 255, -1) # Draw filled contour in mask
		out = np.zeros_like(im) # Extract out the object and place into output image
		out[mask == 255] = im[mask == 255]
		#out = cv2.bitwise_not(out)
		
		cv2.imshow('Output', out)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

		print("Object Area : \n")
		print(objects)

blurred = cv2.pyrMeanShiftFiltering(out, 31, 91)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)		
ret1, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
thresh = cv2.bitwise_not(thresh)
cv2.imwrite(os.path.join(path,"spine.png"),thresh)
cv2.imshow("th",thresh)
# mask = np.zeros_like(thresh)
# cv2.imshow("m",mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()