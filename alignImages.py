# program to find the align images
from __future__ import print_function
import cv2
import numpy as np
from pathlib import Path 
import os
 
MAX_FEATURES = 500
GOOD_MATCH_PERCENT = 0.15
 
 
def alignImages(im1, im2):
 
  # Convert images to grayscale
  #im1Gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
  #im2Gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
   
  # Detect ORB features and compute descriptors.
  orb = cv2.ORB_create(MAX_FEATURES)
  keypoints1, descriptors1 = orb.detectAndCompute(im1, None)
  keypoints2, descriptors2 = orb.detectAndCompute(im2, None)
   
  # Match features.
  matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
  matches = matcher.match(descriptors1, descriptors2, None)
   
  # Sort matches by score
  matches.sort(key=lambda x: x.distance, reverse=False)
 
  # Remove not so good matches
  numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
  matches = matches[:numGoodMatches]
 
  # Draw top matches
  imMatches = cv2.drawMatches(im1, keypoints1, im2, keypoints2, matches, None)
  cv2.imwrite("matches.jpg", imMatches)
   
  # Extract location of good matches
  points1 = np.zeros((len(matches), 2), dtype=np.float32)
  points2 = np.zeros((len(matches), 2), dtype=np.float32)
 
  for i, match in enumerate(matches):
    points1[i, :] = keypoints1[match.queryIdx].pt
    points2[i, :] = keypoints2[match.trainIdx].pt
   
  # Find homography
  h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
 
  # Use homography
  height, width = im2.shape
  im1Reg = cv2.warpPerspective(im1, h, (width, height))
   
  return im1Reg, h
 
 
if __name__ == '__main__':
  input_path = Path("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/patient_masks/patient1/")
  output_path = Path("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/alignedmaskpngs/")
  image_folder = os.listdir(input_path)

  #image1_path = Path("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/maskpngs/binsupimg2.png") 
  #image2_path = Path("C:/Users/sahalab/Desktop/MACHINE LEARNING IN IMAGE PROCESSING/PythonCorey/pngs/maskpngs/binsupimg3.png")
  # Read reference image
  #imReference = cv2.imread(str(image1_path), 0)
 
  # Read image to be aligned
  #im = cv2.imread(str(image2_path), 0)
   
  print("Aligning images ...")
  # Registered image will be resotred in imReg. 
  # The estimated homography will be stored in h. 
  #imReg, h = alignImages(im, imReference)

  #Register each subsequent image and save 
  for i,image in enumerate(image_folder,0):
    if i < 31:
      im1 = cv2.imread(os.path.join(input_path,image_folder[i]),0)
      im2 = cv2.imread(os.path.join(input_path,image_folder[i+1]),0)

      imReg, h = alignImages(im1, im2)


     # Write aligned image to disk. 
      outFilename = os.path.join(output_path,"aligned{}.png".format(i))
      print("Saving aligned image : ", outFilename); 
      cv2.imwrite(outFilename, imReg)
    

    # Print estimated homography
      print("Estimated homography : \n",  h)
  