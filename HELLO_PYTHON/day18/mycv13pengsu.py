import cv2

img_w = cv2.imread('white.png')
img_r = cv2.imread('red.png')


cv2.imshow('img_w', img_w)
cv2.imshow('img_r', img_r)

print(img_r.shape)
ii,jj,c = img_r.shape    # i값 j값 color

i_off = 20   #offset   y축
j_off = 20   #offset   x축

# 크기가 작은 그림 기준을 반복문을 돌렸음
for i in range(ii):
    for j in range(jj):
        img_w[i+i_off ][j+j_off][0]=img_r[i][j][0]
        img_w[i+i_off ][j+j_off][1]=img_r[i][j][1]
        img_w[i+i_off ][j+j_off][2]=img_r[i][j][2]
cv2.imshow('img_w', img_w) 
# 배열에다가 덮어 씌운다는 의미
# rgb 참고 
# 이거 잘 해야함.. 

cv2.waitKey(0)
cv2.destroyAllWindows()



