import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np


cascade_file = 'cascade/haarcascade_frontalface_default.xml'

cascade = cv2.CascadeClassifier(cascade_file)

#검출하기
img = cv2.imread('./image/3.jpg') 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 

img2 = img.copy()
img2 = Image.fromarray(img2)

def kr_putText(img2,text,w,h,r,g,b):
    draw = ImageDraw.Draw(img2)
    # font=ImageFont.truetype("fonts/gulim.ttc",30)
    font=ImageFont.truetype("fonts/H2PORL.TTF",30)
    org=(w,h)
    draw.text(org,text,font=font,fill=(r,g,b))
    named = np.array(img2)
    font=cv2.FONT_HERSHEY_SIMPLEX
    size, BaseLine=cv2.getTextSize(text,font,1,2)
    return named

for idx, (x, y, w, h) in enumerate(face_list):
    cropped = img[y:y+h, x:x+w]
    # cv2.imwrite(f'mem{idx}.jpg', cropped)
    
    print(x,y,w,h)
    color = (0, 0, 225) 
    pen_w = 3 
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w) 
    named = kr_putText(img2, "수지", x+w-150, y+h, 0, 255, 0)
    
cv2.namedWindow('img', cv2.WINDOW_NORMAL)

cv2.imshow('img', named)
cv2.imwrite('temp.jpg', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()