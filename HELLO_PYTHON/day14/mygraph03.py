import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock

ds = DaoStock()

arrx1 = []
arrx2 = [] 
arrx3 = []
arry1 = range(28)
arry2 = range(28)
arry3 = range(28)

arrz1 = ds.selects("삼성전자")
arrz2 = ds.selects("LG")
arrz3 = ds.selects("SK")

for i in range(28):
    arrx1.append(-1)
    arrx2.append(0)
    arrx3.append(1)


fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.plot(arrx1,arry1,arrz1)
ax.plot(arrx2,arry2,arrz2)
ax.plot(arrx3,arry3,arrz3)

plt.show()



