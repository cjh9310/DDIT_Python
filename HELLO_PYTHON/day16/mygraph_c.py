import matplotlib.pyplot as plt
import numpy as np
from day16.daostocksink import DaoStockSink

dss = DaoStockSink()

arrzs = dss.selects()

mylen = len(arrzs[0])   # 0번쨰를 잡아야 갯수가 나옴.  3952 출력됨
print(mylen)

arrx = np.zeros(mylen)
arry = list(range(mylen))    

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

for idx,arrz in enumerate(arrzs):
    ax.plot(arrx+idx,arry,arrz/arrz[0])  
     
plt.show()



