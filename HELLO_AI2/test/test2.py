import cx_Oracle
import os

LOCATION = r"C:\instantclient_21_6"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

db = cx_Oracle.connect("ddit401", "ddit401", "localhost:1521/xe")
cursor = db.cursor()

sql = "insert into AGE values (4, '40~49')"
cursor.execute(sql)

db.commit()
cursor.close()
db.close()