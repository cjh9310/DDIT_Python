import cv2

# 방법1
# img1 = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)
# print("img1",img1)
# cv2.imshow('img1', img1)

# 방법2
img1 = cv2.imread('red.png')    
dst = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print("dst",dst)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

#흑백값
# dst     
# [[123 93]
#  [94 91]
#  [94 91]]

#mycv02의 컬러값
# img1 [[[ 77  72 240]   129
#   [ 37  31 237]]       101
#
#  [[ 39  31 237]        102
#   [ 36  28 237]]       
#
#  [[ 40  32 237]
#   [ 36  28 237]]]

