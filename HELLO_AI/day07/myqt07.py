import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from day07.mymnist_lcp_load_class import AiLCP



# 문제 버튼을 누를 때마다 1씩 감소.

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt07.ui")[0]

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
        com=""
        mine=""
        result=""
        mine = self.le_mine.text()
        

        
        hky = AiLCP()
        
        ans = -1
        if mine == "가위" :
            ans = hky.guess([[0]])
        elif mine == "바위" :
            ans = hky.guess([[0.5]])
        elif mine == "보" :
            ans = hky.guess([[1]])
            
        if ans == 0:
            com = "가위"
        elif ans == 1:
            com = "바위"
        elif mine == 2 :
            com= "보"
            
            
        
        if com == mine :
            result="무승부"
        elif mine == '가위' and com == '바위' or mine == "바위" and com == '보' or mine == "보" and com == '가위' :
            result ="컴퓨터 승"
        else :
            result = "사람 승"
        self.le_com.setText(com)
        self.le_result.setText(result)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    