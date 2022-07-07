# 출력할 구구단을 입력하시오 

# num = input("출력할 구구단을 입력하시오")

# num1 = int(num)
# num2 = list(range(10))


# for i in num2 :
#     print("%d X %d = %d" %(num1,num2,num1*num2))



dan = input("출력할 구구단을 입력하시오")
idan = int(dan)

for i in range(1,9+1) :
    print("{}*{}={}".format(idan,i,idan*i))    # 0부터 실행된다?


# print("{}*{}={}".format(idan,1,idan*1))
# print("{}*{}={}".format(idan,2,idan*2))
# print("{}*{}={}".format(idan,3,idan*3))
# print("{}*{}={}".format(idan,4,idan*4))
# print("{}*{}={}".format(idan,5,idan*5))
# print("{}*{}={}".format(idan,6,idan*6))
# print("{}*{}={}".format(idan,7,idan*7))
# print("{}*{}={}".format(idan,8,idan*8))
# print("{}*{}={}".format(idan,9,idan*9))

