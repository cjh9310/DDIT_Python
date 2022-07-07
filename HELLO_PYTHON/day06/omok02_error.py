import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton


form_class = uic.loadUiType("omok02.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flagWb = True
        self.arr2D = [
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        self.pb2D = []
        self.setupUi(self)
        
        for i in range(10) :  # i가 y축을 결정
            line = []
            for j in range(10) :   #j가 x축을 결정
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setGeometry(j*40, i*40, 40, 40)
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setToolTip("{},{}".format(i,j)) 
                #toolTip으로 마우스를 가져다대면 번호가 달라지는 것을 지정함.
                btn.clicked.connect(self.myclick)
            #   self.pb2D.append(btn)   # btn에 100개 담아줌.
                line.append(btn)
            self.pb2D.append(line)
            
        self.myrender()
        
        self.show()
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j] ==0 :
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                
        
    def myclick(self):
        str_ij = self.sender().toolTip()  #자리 번호 생성
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        # print(i,j)        아래 지우고 실행해보기/
        
        
        # self.arr2D[i][j] = 1 흰돌만 생성됨.
        # self.myrender()
        # 문제 바둑돌 번갈아 생성. 힌트 : true면 1 false면 2를 생성하게 만들어라.
        if self.arr2D[i][j] > 0: # 한 번 있던 돌에 중복으로 생기지 않음
            return # function의 반환값. 
        
        if self.flagWb:  # 돌이 번갈아서 생성됨.
            self.arr2D[i][j] = 1
        else :
            self.arr2D[i][j] = 2
        self.myrender()
        
        self.flagWb = not self.flagWb
        
        
        
        
        # 문제 바둑돌 번갈아 생성.
        # 실패..  실행하면 흰돌 하나만 생성됨.
        # if self.arr2D[i][j] :
        #     self.sender().setIcon(QtGui.QIcon('1.png'))
        # else :
        #     self.sender().setIcon(QtGui.QIcon('2.png'))
        # self.arr2D[i][j] = not self.arr2D[i][j]   
        

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()