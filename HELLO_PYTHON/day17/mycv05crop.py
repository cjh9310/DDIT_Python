import cv2

img1 = cv2.imread('startup.png',cv2.IMREAD_COLOR)

dst = img1[100:500, 400:800].copy()

cv2.imshow('img1', img1)
cv2.imshow('cut image', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()