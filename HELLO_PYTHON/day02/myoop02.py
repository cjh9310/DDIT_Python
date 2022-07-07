class Xi:
    def __init__(self):
        self.money = 1000
    def steal(self,smoney):
        self.money += smoney
       

class Putin :
    def __init__(self):
        self.nuclear = 5000
    def alzheimer(self):
        self.nuclear -= 1
        
        
class JungEun :
    def __init__(self):
        self.missile = 10000
    def ssorau(self):
        self.missile -= 100
        
       
class Sungwoo(Xi,Putin,JungEun) : 
    def __init__(self):
        Xi.__init__(self)
        Putin.__init__(self)
        JungEun.__init__(self)
# https://www.fun-coding.org/PL&OOP1-10.html   In[190] 참고.

s = Sungwoo()
print(s.money)
print(s.nuclear)
print(s.missile)

s.steal(10)
s.alzheimer()
s.ssorau()

print(s.money)
print(s.nuclear)
print(s.missile)


# 자바에서는 상속이 하나  파이썬은 여러개 xi putin JungEun을 다 Sungwoo 안에 상속키기고 차례대로 살행해라