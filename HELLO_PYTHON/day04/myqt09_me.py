import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myqt09.ui")[0]


# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 클릭 시 실행할 function
        self.pb0.clicked.connect(self.myclick0)
        self.pb1.clicked.connect(self.myclick1)
        self.pb2.clicked.connect(self.myclick2)
        self.pb3.clicked.connect(self.myclick3)
        self.pb4.clicked.connect(self.myclick4)
        self.pb5.clicked.connect(self.myclick5)
        self.pb6.clicked.connect(self.myclick6)
        self.pb7.clicked.connect(self.myclick7)
        self.pb8.clicked.connect(self.myclick8)
        self.pb9.clicked.connect(self.myclick9)
        self.pb_call.clicked.connect(self.myclick)
        # 화면을 보여준다.
        self.show()    #awt의 visiable역할

        
    def myclick0(self):
        text = "0"
        self.le.insertPlainText(text)
    def myclick1(self):
        self.le.insertPlainText("1")
    def myclick2(self):
        self.le.insertPlainText("2")
    def myclick3(self):
        self.le.insertPlainText("3")
    def myclick4(self):
        self.le.insertPlainText("4")
    def myclick5(self):
        self.le.insertPlainText("5")
    def myclick6(self):
        self.le.insertPlainText("6")
    def myclick7(self):
        self.le.insertPlainText("7")
    def myclick8(self):
        self.le.insertPlainText("8")
    def myclick9(self):
        self.le.insertPlainText("9")
    
        
    def myclick(self):
        QMessageBox.question(self, 'Message', "통화하시겠습니까?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()