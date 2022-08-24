import numpy as np
from day21_gpu_omok.dao_gibo import DaoGibo
import os


class RaoGibo :
    def __init__(self, file_name):
        self.file_name = file_name
        self.dg = DaoGibo()
        self.gibo = []
        self.gibo_ai = []
        self.ans = []
        self.win= -1
        
        self.flagWb = True
        self.arr2D = np.zeros((20,20),dtype="int")
        
        self.gibo.append(self.oneline(self.arr2D))
        self.gibo_ai.append(self.oneline_ai(self.arr2D))
        
        
        self.gibo2db()
        self.insert_db()
        
    def insert_db(self):
        mymax = self.dg.getPanMax()
        cnt = self.dg.insert("1", self.win, self.gibo, self.gibo_ai, self.ans)
        print("cnt",cnt)


    def getGibo(self):
       
       
       
        arr_i=[]
        arr_j=[]
        
        path_dir = 'D:\workspace_python\HELLO_AI\day21_gpu_omok\Freestyle2'
        f = os.listdir(path_dir)
        # f = open(self.file_name, 'Freestyle2')
        
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
        return mystr
    
    def oneline_ai(self,arr2D):
        mystr = ""
        for i in arr2D:
            for j in i:
                mystr += str(j)
                
        if self.flagWb:
            mystr = mystr.replace("1", "x").replace("2","1")
        else :
            mystr = mystr.replace("2", "x")
        
        return mystr
    
    
    def gibo2db(self):
        arr_i,arr_j = self.getGibo()
        win = -1
        if len(arr_i)%2 == 0 :
            win = 2
        else :
            win = 1
        self.win = win
        
        for idx,i in enumerate(arr_i):
            ii = arr_i[idx]
            jj = arr_j[idx]
            if self.flagWb:
                self.arr2D[ii][jj]=1
            else :
                self.arr2D[ii][jj]=2
            str = self.oneline(self.arr2D)
            str_ai = self.oneline_ai(self.arr2D)
            
            self.gibo.append(str)
            self.gibo_ai.append(str_ai)
            self.ans.append(ii*20+jj)
            
            print(idx,ii,jj,str,str_ai,ii*20+jj,win)
            
            self.flagWb = not self.flagWb   # flagWb가 false로 바뀌어 다음 돌 차례
        
    
    
    
if __name__ == '__main__':
    rg = RaoGibo("Freestyle2")