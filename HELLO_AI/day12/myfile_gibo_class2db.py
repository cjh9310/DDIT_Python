import numpy as np


class RaoGibo :
    def __init__(self):
        self.flagWb = True
        
        self.arr2D = np.zeros((20,20),dtype="int")
        self.gibo2db()

    def getGibo(self):
        file_name = "0_0_1_2.psq"
        arr_i=[]
        arr_j=[]
        f = open(file_name, 'r')
        lines = f.readlines()
        for line in lines:
            arr_split = line.split(",")
            mylen = len(arr_split)
        #    print(mylen,line,end="")    한 줄당 인덱스값 생성
            if mylen == 3:
                try :
                    i = int(arr_split[0])-1
                    j = int(arr_split[1])-1
                    arr_i.append(i)
                    arr_j.append(j)
                except:
                    pass
        f.close()
        return arr_i,arr_j
    
    def oneline(self,arr2D):
        mystr = ""
        for i in arr2D:
            for j in i:
                mystr += str(j)
        return mystrx  1
    def gibo2db(self):
        arr_i,arr_j = self.getGibo()
        for idx,i in enumerate(arr_i):
            ii = arr_i[idx]
            jj = arr_j[idx]
            if self.flagWb:
                self.arr2D[ii][jj]=1
            else :
                self.arr2D[ii][jj]=2
            str = self.oneline(self.arr2D)
            print(idx,ii,jj,str[0:40])
            
            self.flagWb = not self.flagWb   # flagWb가 false로 바뀌어 다음 돌 차례
        
    
    
    
if __name__ == '__main__':
    rg = RaoGibo()