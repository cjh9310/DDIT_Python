import numpy as np
import cv2
import random
from numpy import dtype
import os

labels = [
    "이상권",
    "김유미",
    "박수현",
    "박성우",
    "최재혁",
    "양형주"
  ]

dirs = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5"
      ]

test_label = []
test_image = np.empty((0, 0, 0),np.uint8)

cnt = 0

for i in range(6):
    files = os.listdir("train_eng/"+dirs[i])
    for f in files:
        test_image = np.append(test_image,cv2.imread('train_eng/'+dirs[i]+'/{}'.format(f)))
        test_label.append(i)
        cnt+=1
    
    


test_image = test_image.reshape((cnt,480,640,3))
test_label_n = np.array(test_label)

print(test_image.shape)
print(test_label_n)

np.save("train_image",test_image)
np.save("train_label",test_label_n)





