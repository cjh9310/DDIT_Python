import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                     'haarcascade_frontalface_alt.xml')
# 이미지 불러오기
img = cv2.imread('startup.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
# 영상 출력
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()