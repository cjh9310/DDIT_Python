import cv2

src = cv2.imread('Lenna.jpg')
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    #축소 후
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)
    #복원
dst_01 = mosaic(src)
cv2.imshow('Lenna.jpg', dst_01)

cv2.waitKey(0)
cv2.destroyAllWindows()