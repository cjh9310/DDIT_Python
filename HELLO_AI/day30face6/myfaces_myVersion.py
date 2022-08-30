import cv2
import random
import numpy as np
import glob

labels = ["곽금규",
          "곽동석",
          "기민혁",
          "김미정",
          "김민수",
          
          "김성겸",
          "김유미",
          "박건영",
          "박성우",
          "박수빈",
          
          "박수현",
          "박지영",
          "심재린",
          "양형주",
          "윤재열",
          
          "이상권",
          "이혜림",
          "장재훈",
          "조정현",
          "채희진",
          
          "최재혁",
          "한재웅",
          "한태훈"
          ]

dirs = [
        "00",
        "01",
        "02",
        "03",
        "04",
        
        "05",
        "06",
        "07",
        "08",
        "09",
        
        "10",
        "11",
        "12",
        "13",
        "14",
        
        "15",
        "16",
        "17",
        "18",
        "19",
        
        "20",
        "21",
        "22"
      ]

train_image = np.empty((0, 0, 0), np.uint8)
train_label = []

path = 'train_image/*'
folder_list = glob.glob(path)
for idx, folder in enumerate(folder_list):
    folder = str(folder).replace('train_image\\','')
    
    path2 = 'train_image/{}/*'.format(folder)
    file_list = glob.glob(path2)
    for file in file_list:
        file_name = str(file).replace('\\', '/')
        train_image = np.append(train_image, cv2.imread(file_name))
        train_label.append(idx)
    
train_image = train_image.reshape((len(file_list), 32, 32, 3))

print("success all photo append")
print(train_label)

