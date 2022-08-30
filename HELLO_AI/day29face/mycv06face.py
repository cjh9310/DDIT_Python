import cv2

cascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_alt.xml')

#검출하기
img = cv2.imread('4.png') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
face_list = cascade.detectMultiScale(gray, minSize=(50,50)) 
imgNum = 0

for (x, y, w, h) in face_list:
    cropped = img[y - int(h / 4):y + h + int(h / 4), x - int(w / 4):x + w + int(w / 4)]
    cv2.imwrite("we" + str(imgNum) + ".png", cropped)
    imgNum += 1
    
cv2.imshow('Image view', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
