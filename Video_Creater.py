import os
import cv2

path="images"
images=[]

for file in os.listdir(path):
    name,ext=os.path.splitext(file)
    if ext in [".gif",".png",".jpg",".jpeg",".jfif"]:
        f=path+"/"+file
        images.append(f)


count=len(images)

frame=cv2.imread(images[0])
width,height,channels=frame.shape
size=(height,width)
out=cv2.VideoWriter("project.avi",cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    frame=cv2.imread(images[i])
    out.write(frame)
out.release()
print("Done")



    
