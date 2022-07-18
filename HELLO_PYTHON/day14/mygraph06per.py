import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock
import numpy as np

ds = DaoStock()

arrx = np.zeros(28)

arry = list(range(28))


arr_name = ds.getAllNames()

arrz = []
for n in arr_name:
    arrz.append(ds.selects(n))
    

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

for idx,arr in enumerate(arrz):
    arr_n = np.array(arr)
    print(idx, arr_n,arr_name[idx])
    ax.plot(arrx+idx    ,arry   ,arr_n/arr[0]) # arr를 arr np로 바꾸고 arr의 첫 번째 값으로 나눠줌

plt.show()



