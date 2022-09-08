import cv2
import numpy as np
import os

labels = [ "이상권", "김유미", "박수현", "박성우", "최재혁", "양형주"]

dirs = [
        "0",
        "1",
        "2",
        "3", 
        "4",
        "5"
      ]


#image 가 배열로 들어가있음

train_label = []
train_image = np.empty((0, 0, 0), np.uint8)

cnt = 0
    
for i in range(6):

    files = os.listdir("train_eng/"+dirs[i])
    for f in files:
        train_image = np.append(train_image,cv2.imread('train_eng/'+dirs[i]+'/{}'.format(f)))
        train_label.append(i)
        cnt+=1

train_image = train_image.reshape((cnt,480,640,3))
train_label_n = np.array(train_label)

print(train_image.shape)
print(train_label_n)

np.save("train_image",train_image)
np.save("train_label",train_label)







