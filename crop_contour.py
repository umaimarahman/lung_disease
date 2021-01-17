#this program contours the aorta and find the area of the aorta
import numpy as np
import cv2
import natsort
import os

def locate_aorta(im,count):
    H, W, channels =im.shape
    blurred = cv2.pyrMeanShiftFiltering(im, 31, 91)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(im, contours, -1, (0,0, 255), 2)

    cv2.imwrite('out{}.jpg'.format(count), im)
    listlen = len(contours)
    print(listlen)
    area=[]
    #area stores the area of each object
    for i in range(listlen):
        area.append(cv2.contourArea(contours[i]))

    print("Area of objects : \n"+str(area)+"\n")
    aorta = []
    for i in range(listlen):
        if area[i] > 700 and area[i] < 1000:
        #if area[i] > 800.0 and area[i] < 1700.0:
            aorta_cnt = contours[i]
            idx = i  # The index of the contour that surrounds your object
            mask = np.zeros_like(threshold) # Create mask where white is what we want, black otherwise
            cv2.drawContours(mask, contours, idx, 255, -1) # Draw filled contour in mask
            out = np.zeros_like(img) # Extract out the object and place into output image
            out[mask == 255] = img[mask == 255]
            # Show the output image
            cv2.imwrite(os.path.join(output_path,"aorta_{}.png".format(i)),out)
            cv2.imshow('Output', out)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            cv2.drawContours(im, [aorta_cnt], 0, (0,255,0), 2)
            cv2.imshow('image',im)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            aorta.append(area[i])

    print(i,aorta)
    #print(aorta_cnt)
    return aorta

input_path = "C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/patient_masks/patientsub4/"
output_path = "C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/patient_masks/aorta_p4/"
image_folder = os.listdir(input_path)
image_folder = natsort.natsorted(image_folder,reverse=False)
aorta_loc = []
for index, image in enumerate(image_folder,0):
    img = cv2.imread(os.path.join(input_path,image_folder[index]))
    #calling the locate_aorta() function 
    aorta_loc.append(locate_aorta(img,index))
print("Aorta Area : \n")
print(aorta_loc)



length = len(aorta_loc)
for i in range(length):
    if aorta_loc !=[]:
        sum_of_area = np.cumsum(aorta_loc)

print(sum_of_area[-1])

length = len(sum_of_area[-1])
for i in range(length):
    area_sum = np.cumsum(sum_of_area[-1])

print(area_sum[-1])
avgarea = area_sum/length
print(avgarea[-1])