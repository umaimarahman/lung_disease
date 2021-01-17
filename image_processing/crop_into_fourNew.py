import cv2,time
import cv2
import numpy as np
import os
from PIL import Image
import natsort

def image_crop(img,imageName,folder_name):
    out_folder = "C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/patient_chopped/"
    output_path = os.path.join(out_folder,folder_name)
    print(output_path)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    img2 = img
    index=0
    height, width = img.shape
    # Number of pieces Horizontally 
    CROP_W_SIZE  = 2
    # Number of pieces Vertically to each Horizontal  
    CROP_H_SIZE = 2 
    crop_list = []
    for ih in range(CROP_H_SIZE ):
        for iw in range(CROP_W_SIZE ):
            index+=1
            x = round(width/CROP_W_SIZE * iw )
            y = round(height/CROP_H_SIZE * ih)
            h = round(height / CROP_H_SIZE)
            w = round(width / CROP_W_SIZE )
            print(x,y,h,w)
            img = img[y:y+h, x:x+w]
            crop_list.append(img)
            cv2.imwrite(os.path.join(output_path,"{}_{}".format(index,imageName)),img)
            img = img2

    return crop_list

input_path = "C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/patient_NewMask/"
folder_list =os.listdir(input_path)
patients = len(folder_list)
for k in range(patients):
    image_path = os.path.join(input_path,folder_list[k])
    image_list = os.listdir(image_path)
    num_images = len(image_list)

    if(num_images!=0):

        #image_list = natsort.natsorted(image_list,reverse = False)
        imgarray = np.zeros((512,512))
        # with open("Analyze Average 4.csv", "a") as text_file:
        #     text_file.write("\n AverageTL\t AverageTR\t AverageBL\t Average BR \t Average \tPatient_Name\n")
        cropped_list = []
        #store the 4 images in a list
        for i in range(num_images):
            if image_list[i].find("_Spine_") != -1:
                print(image_list[i])
                path_im = str(os.path.join(image_path,image_list[i]))
      
                img = cv2.imread(path_im,0)
                ret,imgarray = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
                np.set_printoptions(threshold = np.inf)
                print()
                cropped_list = image_crop(img,image_list[i],folder_list[k])
                top_left = cropped_list[0]
                top_right = cropped_list[1]
                bottom_left = cropped_list[2]
                bottom_right = cropped_list[3]

                sum_of_TL= np.cumsum(top_left)
                sum_of_TR= np.cumsum(top_right)
                sum_of_BL= np.cumsum(bottom_left)
                sum_of_BR= np.cumsum(bottom_right)
                
                averageTL = round(sum_of_TL[-1]/top_left.size)
                averageTR = round(sum_of_TR[-1]/top_right.size)
                averageBL = round(sum_of_BL[-1]/bottom_left.size)
                averageBR = round(sum_of_BR[-1]/bottom_right.size)

                imgname = np.array(image_list[i])
                sum_of_bits = np.cumsum(imgarray)
                average = round(sum_of_bits[-1]/imgarray.size)
                print("==========================================================="+str(imgname)+"====================================================")
                #print(sum_of_bits[-1])
                print("AverageTL : \t"+str(averageTL)+"\t AverageTR : \t"+str(averageTR) + "AverageBL : \t"+str(averageBL)+"AverageBR : \t"+str(averageBR)+"\t Average sum : \t"+str(average))

                #Storing average1, average2, average, file_name in a text file
                # with open("Analyze Average 4.csv", "a") as text_file:
                #             text_file.write("\n"+str(averageTL)+"\t\t"+ str(averageTR)+"\t\t"+str(averageBL)+"\t\t"+ str(averageBR) +"\t\t"+str(average)+ "\t\t" + str(image)+"\n")



