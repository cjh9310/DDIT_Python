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

test_label = []
test_image = np.empty((0, 0, 0), np.uint8)

cnt = 0
    
for i in range(6):

    files = os.listdir("test_image/"+dirs[i])
    for f in files:
        test_image = np.append(test_image,cv2.imread('test_image/'+dirs[i]+'/{}'.format(f)))
        test_label.append(i)
        cnt+=1

test_image = test_image.reshape((cnt,128,128,3))
test_laben = np.array(test_label)

print(test_image.shape)
print(test_label)

np.save("test_image",test_image)
np.save("test_label",test_label)







