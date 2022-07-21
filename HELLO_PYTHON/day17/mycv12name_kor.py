import cv2

img1 = cv2.imread('startup.png')
# 폰트 색상 지정
blue = (255, 0, 0)
# 폰트 지정
font =  cv2.FONT_HERSHEY_PLAIN
 
# 이미지에 글자 합성하기
img = cv2.putText(img1, "수지", (470,200), font, 2, blue, 1, cv2.LINE_AA)
# 한글을 쓰면 ???? 라는 오류가 뜬다 opencv를 이용하면서 한글이 깨지기 때문에 PIL를 활용하면 된다.



cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

