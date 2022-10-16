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


result = []

for i, hangul in enumerate(rows):
    left = str(hangul).replace("(", "")
    right = str(left).replace(")", "")
    comma = str(right).replace(",", "")
    dot = str(comma).replace("'", "")

    result += [dot]

print(result)
for i in result:
    print(i)

cursor.close()
connect.close()