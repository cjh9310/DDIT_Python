import numpy as np

def changeInt(a):
    a = 3
    
def changeNumpye(a):
    a[0]=3

    
b = 1
bb = np.ones((2))

print(b)
print(bb)
changeInt(b) 
changeNumpye(bb)
print(b)
print(bb[0])

