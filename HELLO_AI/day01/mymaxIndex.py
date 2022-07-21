arr =  [0,1,3,1,1, 1,2,2,2,2]


# index 2를 출력하게 하라 (2는 index값이고, index 2에 들어가있는 3이란 값이 arr배열에서 가장 큰 수이다) 
#-1 한 이유! 배열내 수가 모두 0포함 자연수라서 그거보다 작은 것을 대충적어줌 

max = -1 

for i in arr:
    if max < i:
        max = i

print("max",max)

myidx = -1

for idx,i in enumerate(arr):
    if max == i:
        myidx = idx
        
print("myidx",myidx) 

#2