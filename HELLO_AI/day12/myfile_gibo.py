# 파일 내부의 숫자 정보만 뽑아오기
f = open("0_0_1_2.psq", 'r')
lines = f.readlines()
for line in lines:
    arr_split = line.split(",")
    mylen = len(arr_split)
#    print(mylen,line,end="")    한 줄당 인덱스값 생성
    if mylen == 3:
        try :
            i = int(arr_split[0])
            j = int(arr_split[1])
            print(i,j)  # mylen line,end="" 와 같음
        except:
            print("error")
f.close()