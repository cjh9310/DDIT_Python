class Xi:
    def __init__(self):  # 변수
        self.money = 1000
    def steal(self, smoney): # 메소드
        self.money += smoney

class Putin:
    def __init__(self):
        self.nuclear = 5000
    def alzheimer(self):
        self.nuclear -= 1

class JungEun:
    def __init__(self):
        self.missile = 10000
    def ssorau(self):
        self.missile -= 100

class Child(Xi, Putin, JungEun): 
    def __init__(self):
        Xi.__init__(self) #변수를 가져옴
        Putin.__init__(self) #변수를 가져옴
        JungEun.__init__(self) #변수를 가져옴
        
    #메소드 오버라이딩이란 상속받은 부모 클래스의 메소드를 재정의하여 사용하는 것을 의미합니다.
    def steal(self, smoney):  #메소드를 가져옴 (오버라이딩)
        super().steal(smoney)
        
    def alzheimer(self):      #메소드를 가져옴 (오버라이딩) 
        super().alzheimer()
        
    def ssorau(self):         #메소드를 가져옴 (오버라이딩)
        super().ssorau()
        
ch = Child()
    #f는 printf기능 중괄호가 %d 역할을 함
print(f"money : {ch.money}, nuclear : {ch.nuclear}, missile : {ch.missile}")
ch.steal(100)
ch.alzheimer()
ch.ssorau()
print(f"money : {ch.money}, nuclear : {ch.nuclear}, missile : {ch.missile}")