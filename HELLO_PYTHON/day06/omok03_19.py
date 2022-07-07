import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.Qt import QIcon, QPushButton
from idlelib import tooltip
from msilib.schema import ComboBox


form_class = uic.loadUiType("omok03.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flagWb = True
        self.flagIng = True # 돌이 5개 이후에 더이상 놓아지지 않는다.
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0]
        ]
        
        self.pb2D = []
        
        self.setupUi(self)
        
        for i in range(19):
            line = []
            for j in range(19):
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setGeometry(j*40, i*40, 40, 40)
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setToolTip("{},{}".format(i,j))
                btn.clicked.connect(self.myclick)
                line.append(btn)
            self.pb2D.append(line)
        
        self.myrender()
        self.pbReset.clicked.connect(self.myreset)
        self.arr2D 
        
        self.show()
        
    def myreset(self):
        
        for i in range(19):
            for j in range(19):
                self.arr2D[i][j]=0
                
        self.myrender()
        self.flagWb = True
        self.flagIng = True

    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                               
                
    def myclick(self):
        if not self.flagIng :   # 돌이 5개 이후에 더이상 놓아지지 않는다.
            return 
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        if self.arr2D[i][j] > 0:
            return
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
        up = self.checkUP(i,j,stone) #(i,j,stone)  좌표랑 돌 번호
        dw = self.checkDW(i,j,stone)
        ri = self.checkRI(i,j,stone)
        le = self.checkLE(i,j,stone)
        dr = self.checkDR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        ul = self.checkUL(i,j,stone)
        ur = self.checkUR(i,j,stone)
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = le + ri + 1
        d4 = ul + dr + 1
        
        self.myrender() # 랜더가 먼저 실행되는 이유는?
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.flagIng = False # 돌이 5개 이후에 더이상 놓아지지 않는다. 
            if self.flagWb:
                QMessageBox.question(self, '오목', "흰돌승리", QMessageBox.Yes, QMessageBox.NoButton)
                
            else:
                QMessageBox.question(self, '오목', "흑돌승리", QMessageBox.Yes, QMessageBox.NoButton)
                
        
        
        self.flagWb = not self.flagWb
    
    def checkUR(self,i,j,stone):
        cnt =0
        try: 
            while True :
                i -= 1
                j += 1
                if j<0 :  
                    return cnt
                if i<0 :  
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :  
            return cnt
    
    def checkUL(self,i,j,stone):
        cnt =0
        try: 
            while True :
                i -= 1
                j -= 1
                if j<0 :  
                    return cnt
                if i<0 :  
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :  
            return cnt
        
    def checkDL(self,i,j,stone):
        cnt =0
        try: 
            while True :
                i += 1
                j -= 1
                if j<0 :  
                    return cnt
                if i<0 :  
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :  
            return cnt
    
    def checkDR(self,i,j,stone):
        cnt =0
        try: 
            while True :
                i += 1
                j += 1
                if j<0 :  
                    return cnt
                if i<0 :  
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :  
            return cnt
    
    def checkLE(self,i,j,stone):
        cnt =0
        try: 
            while True :
                j += 1
                if j<0 :  
                    return cnt
                if i<0 :  
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :  
            return cnt
    
    
    def checkRI(self,i,j,stone):
        cnt =0
        try: 
            while True :
                j -= 1
                if j<0 :  
                    return cnt
                if i<0 :  
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :  
            return cnt
        
        
    def checkUP(self,i,j,stone):
        cnt =0
        while True :
            i -= 1
            if i<0 :  #오류1 해결방법
                return cnt
            if j<0 :  
                return cnt
            if self.arr2D[i][j] == stone :
                cnt += 1
            else :
                return cnt
    # 오류1. 젤 위를 찍고 아래를 찍으면 0이 뜨지만 아래부터 찍고 위에를 찍어주면 2개처리 됨.
    # 돌 색은 동일해야함.    (myarr01.py 참고)   
    
    def checkDW(self,i,j,stone):
        cnt =0
        try: #오류2
            while True :
                i += 1
                if i<0 :  #오류1 해결방법
                    return cnt
                if j<0 :  
                    return cnt
                if self.arr2D[i][j] == stone :
                    cnt += 1
                else :
                    return cnt
        except :  #오류2
            return cnt  #오류2
    # 오류2. 마지막 줄에 클릭하면 팅기는 현상 try 예외처리 방법으로 해결해줌.
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()