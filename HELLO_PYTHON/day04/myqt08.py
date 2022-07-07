import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt08.ui")[0]


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
        
        first = self.le_first.text()
        last = self.le_last.text()
        num1 = int(first)
        num2 = int(last)
        txt=""
        for i in range(num1,num2+1) :
            txt+=self.drawStar(i)   # self. 적용
            
        self.te.setText(txt)
        
    def drawStar(self,cnt):        
        ret=""
        for i in range(cnt) :
            ret +="*"
        ret+="\n"
        return ret
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()