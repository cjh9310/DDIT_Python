import time
class Cat :
    def __init__(self):       # 생성자
        print("constructor")

    def crying(self):
        print("crying")
    
    def __del__(self):        # 소멸자
        print("destroyer")    # __init__ 이 아닌데 출력된다?  
# 자바는 가비지 컬렉션이 있어서 자동으로 썻던 메모리를 정리해준다.
# 나머지는 

    def __str__(self):
        return "babo"

c = Cat()
c.crying()       # c.crying()가 없으면 print("crying")는 출력되지 않음.
time.sleep(4)    # sleep사이에는 초단위 # 4초 뒤에 __del__이 출력됨
print(c)         # __del__ 은 기능을 끄는 방식이라 마지막에 출력되고 꺼진다.
