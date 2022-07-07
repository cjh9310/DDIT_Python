def addminmuldiv(a,b) :
    return a+b,a-b,a*b,a/b

sum,min,mul,div = addminmuldiv(1,6)

print("sum",sum)
print("min",min)
print("mul",mul)
print("div",div)

sum = addminmuldiv(1,6) # 배열은 아니지만 배열과 같은 특성을 가지고 있어서 출력할때 전체출력 혹은 부분 출력이 가능하다. 튜플
                        # 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
                        # 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.

print("sum",sum,sum[0])
# print("min",min)
# print("mul",mul)
# print("div",div)
