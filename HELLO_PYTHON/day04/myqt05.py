import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import random

# 문제 버튼을 누를 때마다 1씩 감소.

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt05.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 클릭 시 실행할 function
        self.pb.clicked.connect(self.myclick)
        # 화면을 보여준다.
        self.show()    #awt의 visiable역할
    def myclick(self):
        # me = self.le_mine.text()
        # com = self.le_com.text()
        # self.le_com.text(com)
        # result = ""
        # rnd = random()
        # if(rnd >0.5):
        #     com ="홀"
        # else :
        #     com ="짝"
        # if(com == me) :
        #     result = "승리"
        # else :
        #     result = "패배"
        #
        # self.le_result.text(result)
        
        com = ""
        mine = ""
        result = ""
        
        mine = self.le_mine.text()
            
        rnd = random.random()
        
        if rnd >0.5:
            com ="홀"
        else :
            com ="짝"
        if com == mine :
            result = "승리"
        else :
            result = "패배"
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
        
        
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()