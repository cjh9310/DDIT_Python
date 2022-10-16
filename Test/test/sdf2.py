import cx_Oracle
import os
import re

LOCATION = r"C:\instantclient_21_6"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록
connect = cx_Oracle.connect("team1_202204F","java","112.220.114.130:1521/xe")
cursor = connect.cursor()

sql = f"""
    SELECT A.IND_ID
    FROM IND_MEMBER A
    JOIN CAREER B
    ON A.IND_ID = B.IND_ID
"""
cursor.execute(sql)
rows=cursor.fetchall()
result = ' '.join(str(s) for s in rows)
print(result)
#('test123',) ('winter',) ('dd11',)
str1 = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", result)
print(str1.split())

cursor.close()
connect.close()