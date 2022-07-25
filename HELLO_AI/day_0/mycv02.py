import cv2

img1 = cv2.imread('r.png')
print("img1",img1)
cv2.imshow('img1', img1)

# 77  72 240  RED
# 77 163  61  GREEN
# 189  84  61  BLUE


cv2.waitKey(0)
cv2.destroyAllWindows()

# 배열과 넘피배열의 차이점은 ,  실행시 확인 가능