class Animal :
    def __init__(self):
        self.age =1
    def happyBirth(self):
        self.age+=1
        
class Human(Animal):
    def __init__(self):
        super().__init__()
        # 'Human' object has no attribute 'age' : super가 없으면 왼쪽 오류가 뜬다.
        # 부모에게 상속받아 실행이 안되는 듯
        self.money=10000
    def albamon(self):
        self.money +=1


a = Human()
print(a.money)
print(a.age)

a.happyBirth()
a.albamon()

print(a.money)
print(a.age)





