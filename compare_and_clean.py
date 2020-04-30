import os
import cv2
from tqdm import tqdm
import numpy as np
from skimage import measure
import shutil
os.mkdir("movin")
def mse(imageA,imageB):
   err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
   err /= float(imageA.shape[0] * imageA.shape[1])
   return err
def convert2gray(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

path="folder/"
images=os.listdir(path)
for i,img in tqdm(enumerate(images)):
    if(i==0):
        pass
    else:
     j=i*5
     nameA="try0tis{}.png".format(j)
     path_to_imageA=os.path.join(path,nameA)
     imageA=cv2.imread(path_to_imageA)
     imageA=convert2gray(imageA)
     nameB="try0tis{}.png".format(j+5)
     path_to_imageB=os.path.join(path,nameB)
     imageB=cv2.imread(path_to_imageB)
     imageB=convert2gray(imageB)
     s=measure.compare_ssim(imageA,imageB)
     if(s>0.5):
         shutil.move(path_to_imageA,"movin/")
         print("[] "+path_to_imageA+" moved")
     print(s)
     

