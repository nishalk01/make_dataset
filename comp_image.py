import numpy as np
import cv2
imageA=cv2.imread("image.jpg")
print(imageA.shape)
imageA=cv2.cvtColor(imageA,cv2.COLOR_BGR2GRAY)
imageB=cv2.imread("images.png")
imageB=cv2.resize(imageB,(225,225))
imageB=cv2.cvtColor(imageB,cv2.COLOR_BGR2GRAY)
imageA=imageB
from skimage import measure 
def mse(imageA,imageB):
   err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
   err /= float(imageA.shape[0] * imageA.shape[1])
   return err

m=mse(imageA,imageB)#ssim is better but is inverse meaning returns less value if images are totally different
print(m)
s=measure.compare_ssim(imageA,imageB)
print(s)