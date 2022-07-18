import cv2
# 방법1
# img1 = cv2.imread('startup.png')
# width,height = img1.shape[:2]
#
# M = cv2.getRotationMatrix2D((width/2.0, height/2.0),45,1)
# img_rotation = cv2.warpAffine(img1, M, (width,height))
#
# cv2.imshow('img_rotation', img_rotation)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#방법2
src = cv2.imread("startup.png", cv2.IMREAD_COLOR)

height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2,height/2) # 기준점
                                  , 45 # 회전각도
                                  , 1) # 배율 
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()