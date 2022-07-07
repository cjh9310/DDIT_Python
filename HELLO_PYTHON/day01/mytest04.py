a = input("첫수를 입력하시오.")
b = input("둘째수를 입력하시오.")

aa = int(a)
bb = int(b)

arr = range(aa,bb+1)

sum =0
# for i in arr :
#     sum+=i
# print("%d에서%d까지의 합은 %d입니다." %(aa,bb,sum))

for i in range(aa,bb+1) :
    sum+=i
print("%d에서%d까지의 합은 %d입니다." %(aa,bb,sum))
