import cv2 
import random
from _random import Random

labels = [ "김유미", "박성우", "박수현", "양형주", "이상권", "최재혁" ]

reverses = [ False, False, False, False, False, False ]
    
def saveImage(label, dir, reverse):

    vidcap = cv2.VideoCapture('movie/{}.mp4'.format(label))
    
    print('movie/{}.mp4'.format(labels[idx]))
    
    count = 0
    folder_name = str(dir)[1:3]
    
    while(vidcap.isOpened()):
        ret, src = vidcap.read()
        
        if not ret:
            break
         
        height, width, channel = src.shape
        matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
        dst = cv2.warpAffine(src, matrix, (width,height))
        
        img_save = None
        
        if reverse:
            img_save = dst
        else:
            img_save = src
        path = ""
        if random.random() > 0.16:
            path = "train_image"
        else:
            path = "test_image"
        
        resize_img = cv2.resize(img_save, (128, 128))
        
        cv2.imwrite("{}/{}/{}.png".format(path, folder_name, count), resize_img)
            
        print("{}/{}/{}.png".format(path, folder_name, count))
        
        count += 1
        # if count > 5:
        #     break
    vidcap.release()

## 함수 호출부
for idx, dir in enumerate(range(100, 106)):
    saveImage(labels[idx], dir, reverses[idx])















