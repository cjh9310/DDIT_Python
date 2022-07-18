import numpy as np

arr = range(100)
arr1 = list(range(100))

arr_n = np.array(arr)

arr_n1010 = np.reshape(arr_n,(5,20))

# print("arr",arr)
# print("arr1",arr1)
print("arr_n",arr_n)
print("arr_n1010",arr_n1010)  # 10씩 묶음