# 배열과 numpy 복습 
import numpy as np
arr= [0,1,3,1,1, 1,2,2,2,2]

a = np.max(arr)
print("a",a)
 
a1 = np.min(arr)
print("a1",a1)

b = np.argmax(arr)
print("b",b)