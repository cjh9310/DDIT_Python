import cv2

img1 = cv2.imread('startup.png')
# 폰트 색상 지정
blue = (255, 0, 0)
green= (0, 255, 0)
red= (0, 0, 255)
white= (255, 255, 255) 
# 폰트 지정
font =  cv2.FONT_HERSHEY_PLAIN
 
# 이미지에 글자 합성하기
img = cv2.putText(img1, "수지", (470,200), font, 2, blue, 1, cv2.LINE_AA)


cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

