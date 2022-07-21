import cv2
img = cv2.imread('Lenna.png')
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #회색으로 바꿔줌
cv2.imshow('img', dst)
cv2.imwrite('Lenna.jpg', dst) 
cv2.waitKey(0)
cv2.destroyAllWindows()