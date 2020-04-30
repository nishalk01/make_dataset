path="try_vid/"
import os
import cv2
folders=os.listdir(path)
for j,folder in enumerate(folders):
   os.mkdir(folder)
   path_to_folder=os.path.join(path,folder)
   anime_vid=os.listdir(path_to_folder)
   for vid in anime_vid:
     path_to_videos=os.path.join(path_to_folder,vid)
     cam=cv2.VideoCapture(path_to_videos)
     i=0
     while True:
       ret,image=cam.read()
       if ret:
         i=i+1
         print(folder)
         name="try{}tis{}.png".format(j,i)
         folder_name=os.path.join(folder,name)
         if(i%5==0):
           print("[]"+folder_name+" saved")
           cv2.imwrite(folder_name,image)
           
         
       else:
         print("=====================================================================================================================")
         print(folder+" done")
         print("=====================================================================================================================")
         break
