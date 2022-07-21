import cv2

img1 = cv2.imread('startup.png')

resize_img = cv2.resize(img1, (500, 500))
print("resize_img.shape = {0}".format(resize_img.shape))

cv2.imshow('img1', resize_img)
cv2.imwrite('statup_size.jpg', resize_img) 
cv2.waitKey(0)
cv2.destroyAllWindows()

