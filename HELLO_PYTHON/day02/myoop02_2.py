class Xi:
    def __init__(self):
        super().__init__()
        self.money = 1000
    def steal(self,smoney):
        self.money += smoney
       

class Putin :
    def __init__(self):
        super().__init__()
        self.nuclear = 5000
    def alzheimer(self):
        self.nuclear -= 1
        
        
class JungEun :
    def __init__(self):
        super().__init__()
        self.missile = 10000
    def ssorau(self):
        self.missile -= 100
        
       
class Sungwoo(Xi,Putin,JungEun) : 
    def __init__(self):
        super().__init__()
       #Xi.__init__(self)
        #Putin.__init__(self)
        #JungEun.__init__(self)
        
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
