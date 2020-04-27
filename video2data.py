import cv2
imag=[]
cam=cv2.VideoCapture('y2mate.com - one_punch_man_official_trailer_2JAElThbKrI_720p.mp4')
i=0
while True:
    ret,image=cam.read()
    if ret:
         #print(i)
         i=i+1
        # cv2.imshow('img',image)
         #name="image"
         name="opm_try{}im.png".format(i)
         path='folder/'+name
         print(path)
         if(i%5==0):
           print(i)
           print("saved")
           cv2.imwrite(path,image)
         #print(image)
        
    else:
        break