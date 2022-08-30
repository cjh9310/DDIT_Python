import cv2
import numpy as np
import os

labels = [ "김유미", "박성우", "박수현", "양형주", "이상권", "최재혁" ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "04",
        "05"
      ]



#image 가 배열로 들어가있음

train_label = []
train_image = np.empty((0, 0, 0), np.uint8)

cnt = 0

    
    
for i in range(6):

    files = os.listdir("train_image/"+dirs[i])
    for f in files:
        train_image = np.append(train_image,cv2.imread('train_image/'+dirs[i]+'/{}'.format(f)))
        train_label.append(i)
        cnt+=1
        

train_image = train_image.reshape((cnt,128,128,3))
train_label = np.array(train_label)

np.save("train_image",train_image)
np.save("train_label",train_label)







