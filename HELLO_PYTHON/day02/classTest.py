#베이스 클래스(부모 클래스)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName1(self):
        return "Class Person"
    
    def printInfo(self):
        print("name = {}, age = {}".format(self.name,  self.age) )
        
#파생 클래스(자식 클래스)   
class footballPlayer(Person):
    def __init__(self, name, age, job, level):
        self.job = job
        self.level = level
        super().__init__(name, age) #Person 클래스 초기화
        
    def getSkillLevel(self):
        return self.level
    
    def getName2(self):
        return "Class footballPlayer"    
    
    def printInfo(self):     #메소드 오버라이딩(Overriding)
        super().printInfo()  #name, age는 베이스 클래스 메소드 이용(코드 재활용)
        print("job = {}".format(self.job ))
        
#파생 클래스(자식 클래스)      
class computerEngineer(Person):
    def __init__(self, name, age, job):
        self.job = job
        super().__init__(name, age)  #Person 클래스 초기화      
        
    def getName3(self):
        super().getName1()           
        
    #메소드 오버라이딩(Overriding), age, name은 베이스클래스와 중복임            
    def printInfo(self):  
        print("name = {}, age = {}, job = {}".format(self.name,  
                    self.age, self.job) )        
 
 
print("")
#객체 생성/초기화/출력
p1 = footballPlayer("Mike", 34, "football.player", 99) 
print("name = ", p1.name, ", age = ", p1.age, ", job = ", p1.job, ", level = ", p1.level)
 
#객체 생성/초기화/출력
p2 = computerEngineer("Mark", 28, "computer.enginner")        
print("name = ", p2.name, ", age = ", p2.age, ", job = ", p2.job)
 
 
#super() 함수 예
print("p1.getName2 = ", p1.getName2()) #자신의 메소드 호출
print("p2.getName1 = ", p2.getName1()) #베이스 클래스 메소드 호출(참조)
 
#메소드 오버라이딩(Overriding)
#베이스 클래스에 있는 printInfo() 메소드를 재정의 함
print("")
p1.printInfo()  #베이스(Person) 클래스의 printInfo()도 함께 호출(코드 재사용)
p2.printInfo()  #computerEnginner 클래스의 printInfo()만 호출

