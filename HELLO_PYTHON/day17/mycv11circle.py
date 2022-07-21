import cv2

img1 = cv2.imread('Lenna.png')

cv2.circle(img1, (300, 300), 100, (255, 0, 0), 3, cv2.LINE_AA)
#                 X축   Y축   크기  (    색상   ) 선 두깨
cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()