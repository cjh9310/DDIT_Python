
# 1. 첫수를 입력하시오
# 2. 둘째수를 입력하시오
# 3. 3과 5의 합은 8입니다.

a = input("첫수를 입력하시오.")
b = input("둘째수를 입력하시오.")

aa = int(a)
bb = int(b)

sum = aa + bb

print(str(aa)+"와"+str(bb)+"의 합은"+str(sum)+"입니다")   #방법1
print("%d와%d의 합은 %d입니다." %(aa,bb,sum))             #방법2
# print(aa+"와"+bb+"의 합은"+sum+"입니다.")                 #방법3