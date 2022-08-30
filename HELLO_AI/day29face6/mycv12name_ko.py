import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

src = cv2.imread("image/startup.png")

img = src.copy()
img = Image.fromarray(img)

def kr_putText(img,text,w,h,r,g,b):
    draw = ImageDraw.Draw(img)
    # font=ImageFont.truetype("fonts/gulim.ttc",30)
    font=ImageFont.truetype("fonts/H2PORL.TTF",30)
    org=(w,h)
    draw.text(org,text,font=font,fill=(r,g,b))
    named = np.array(img)
    font=cv2.FONT_HERSHEY_SIMPLEX
    size, BaseLine=cv2.getTextSize(text,font,1,2)
    return named

named = kr_putText(img, "수지", 490, 170, 0, 255, 0)
named = kr_putText(img, "주혁", 660, 70, 0, 255, 0)
named = kr_putText(img, "도완", 220, 90, 255, 0, 0)
named = kr_putText(img, "수빈", 880, 110, 0, 0, 255)
named = kr_putText(img, "스테파니", 1060, 120, 0, 255, 0)
    
cv2.imshow("named_image", named) 

cv2.waitKey()
cv2.destroyAllWindows()

