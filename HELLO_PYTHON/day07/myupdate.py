import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
curs = conn.cursor()
e_id = '3'
e_name = '4'
sex = '4'
addr = '4'

sql = f"""
update
    emp
set
    e_name = '{e_name}',
    sex = '{sex}',
    addr = '{addr}'
where
    e_id = '{e_id}'

"""
cnt = curs.execute(sql)
print(cnt)
conn.commit()
 
conn.close()