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
    ax.plot(arrx+idx,arry,arr)

plt.show()



