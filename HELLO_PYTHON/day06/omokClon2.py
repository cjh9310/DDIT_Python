import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton

form_class = uic.loadUiType("omok02.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.arr2D = [
            [0,1,2,0,0, 0,0,0,0,0],
            [0,2,1,1,2, 0,0,0,0,0],
            [0,0,2,0,0, 0,0,0,0,0],
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
        
        for j in range(10) :
            line = []
            for i in range(10) :  
                btn = QPushButton('', self)
                btn.setIcon(QtGui.QIcon('0.png'))
                btn.setGeometry(i*40, j*40, 40, 40)
                btn.setIconSize(QtCore.QSize(40,40))
                btn.clicked.connect(self.myclick)
            #   self.pb2D.append(btn)   # btn에 100개 담아줌.
                line.append(btn)
            self.pb2D.append(line)
        self.myrebder()
                           
        
        self.show()
    
    def myrebder(self):
        #pb2D[5]  = 5번째자리 6번 
        self.pb2D[5][1].setIcon(QtGui.QIcon('1.png')) # 6번째 자리에 1.png가 적용됨
        
    def myclick(self):
        if self.flagWb :
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else :
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flagWb = not self.flagWb
        

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()