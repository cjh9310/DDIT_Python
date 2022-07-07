import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# 문제 버튼을 누를 때마다 1씩 감소.

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt02.ui")[0]

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
        # self.count += -1                   버튼을 누르면 종료됨...?
        # self.le.setText(str(self.Count))
        
        a = self.le.text()
        aa = int(a)
        aa += -1
        self.le.setText(str(aa))
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()