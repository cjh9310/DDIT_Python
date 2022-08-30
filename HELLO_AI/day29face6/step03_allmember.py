import cv2
import keras
import numpy as np
from PIL import ImageFont, ImageDraw, Image

labels = [ "김유미", "박성우", "박수현", "양형주", "이상권", "최재혁" ]

model = keras.models.load_model('6face.h5')

cascade_file = 'cascade/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_file)

#검출하기
img = cv2.imread('./image/3.jpg') 

font = ImageFont.truetype("./fonts/H2PORL.TTF", 50)
img_pil = Image.fromarray(img)
idraw = ImageDraw.Draw(img_pil)



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
face_list = cascade.detectMultiScale(gray, minSize = (50,50)) 

for idx,(x, y, w, h) in enumerate(face_list):
    cropped = img[y:y+h, x:x+w]
    
    resize_img = cv2.resize(cropped, (128, 128))
    print(resize_img.shape)
    resize_img = np.reshape(resize_img,(1,128,128,3))
    test_images = resize_img/255.0
    
    predictions = model.predict(test_images)
    
    idx_label= np.argmax(predictions[0])
    print(labels[idx_label])
    print(x,y,w,h)
    color = (0, 0, 225) 
    pen_w = 3     
    cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness = pen_w) 
    
    idraw.text((x, y),  labels[idx_label], font=font, fill=(0,0,255,0))
    img = np.array(img_pil)
    
cv2.imshow('img', img)
cv2.imwrite('temp.jpg', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()
