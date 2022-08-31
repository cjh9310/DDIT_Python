import numpy as np


arr_n = np.array([0,0,0,3,3,3,3,3,0,0,0,0,0])

def cutMute(arr_n):
    idx_f = 0
    while True:
        if arr_n[idx_f]<1 :
            pass
        else:
            break
        idx_f+=1
    
    idx_f -=1
    
    
    idx_l = len(arr_n)-1
    while True:
        if arr_n[idx_l]<1 :
            pass
        else:
            break
        idx_l-=1
    idx_l +=2
    
    return arr_n[idx_f:idx_l]
    
arr_n_trim = cutMute(arr_n)
print(arr_n_trim)