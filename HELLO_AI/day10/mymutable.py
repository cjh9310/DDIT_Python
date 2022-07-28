def changeInt(a):
    a = 3
    
def changeArr(a):
    a[0]=3
    
b = 1
bb = [1]

print(b)
print(bb[0])
changeInt(b) # 이미 int라 안변함
changeArr(bb)
print(b)
print(bb[0])