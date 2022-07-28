
arr = [1,2,3]
brr = arr

# shallow copy

arr[0] = 3

print("arr",arr)
print("brr",brr)

# 예상 brr은 그대로 arr만 바뀔듯?
# 결과 arr과 brr은 같은 답