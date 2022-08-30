
import cv2
import random

labels = ["김유미","박성우","박수현","양형주","이상권","최재혁"]


reverses = [
        False,
        False,
        True,
        True,
        True,
        True]

def saveImage(label,reverse):
    try:
        vidcap = cv2.VideoCapture('movie/{}.mp4'.format(label))
        
        count = 0
        while(vidcap.isOpened()):
            ret, src = vidcap.read()
        
            height, width, channel = src.shape
            matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
            dst = cv2.warpAffine(src, matrix, (width, height))
        
            print(dst.shape)
            img_save = None
            if reverse:
                img_save = dst
            else:
                img_save = src
                
            path = "test_image" 
            # if random.random() > 0.16:
            #     path = "train_image"  
            # else:
            #     path = "test_image"  
                
            resize_img = cv2.resize(img_save, (32, 32))    
                
            cv2.imwrite("{}/{}.png".format(path,count), resize_img)    
            
            count += 1
            # if count > 10:
            #     break
        
        vidcap.release()
        
    except:
        pass    

for i in range(6):
    saveImage(labels[i],reverses[i])




