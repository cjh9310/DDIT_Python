import cv2

src = cv2.imread("Lenna.png", cv2.IMREAD_COLOR)  # 입력 이미지(src)
dst = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)
#            커널 크기(ksize), 고정점(anchor), 테두리 외삽법(borderType)

cv2.imshow('img1', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

