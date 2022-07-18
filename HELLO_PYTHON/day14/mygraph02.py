import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
from day14.daostock import DaoStock

ds = DaoStock()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot([ds.price,0,0],[0,1,2],[0,2,0])
ax.plot([1,1,1],[0,1,2],[0,2,0])
ax.plot([-1,-1,-1],[0,1,2],[0,2,0])




plt.show()