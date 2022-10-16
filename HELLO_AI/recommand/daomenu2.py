import pymysql
import numpy as np
import cx_Oracle
import os
import re

LOCATION = r"C:\instantclient_21_6"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록

class DaoMenu:
    def __init__(self):
        self.connect = cx_Oracle.connect("team1_202204F","java","112.220.114.130:1521/xe")

        self.cursor = self.connect.cursor()
        
    def getGroupMenu(self):
        sql = f"""
                SELECT A.IND_ID
                FROM IND_MEMBER A
                JOIN CAREER B
                ON A.IND_ID = B.IND_ID

                """
        self.cursor.execute(sql)
        rows=self.cursor.fetchall()
        result = ' '.join(str(s) for s in rows)
        #('test123',) ('winter',) ('dd11',)
        str1 = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", result)
        ret_arr = str1.split()
        return ret_arr
        
        
    def getMenu(self,CRR_SECTOR):
        sql = f"""
                SELECT A.IND_ID
                FROM IND_MEMBER A
                JOIN CAREER B
                ON A.IND_ID = B.IND_ID
                WHERE
                    CRR_SECTOR = '{CRR_SECTOR}'
                """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        result = ' '.join(str(s) for s in rows)
        #('test123',) ('winter',) ('dd11',)
        str1 = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", result)
        ret_arr = str1.split()
        return ret_arr
        
    def myidx(self, labels, menu):
        idx = -1
        for idx, l in enumerate(labels):
            if l ==menu:
                return idx
                
            
    def labeling(self, labels, menus):
        arr = []
        for m in menus:
            idx = self. myidx(labels, m)
            arr.append(idx)
        
        return arr
    
    def makeDataSets(self, list):
        t_arr = []
        l_arr = []
        for i in range(len(list)-2):
            t_arr.append([list[i],list[i+1]])
            l_arr.append(list[i+2])
        return t_arr,l_arr

    
    def __del__(self):
        # self.curs.close()
        # self.conn.close()
        pass

    
if __name__ == '__main__':
    de = DaoMenu()
    labels = de.getGroupMenu()
    print(labels)
    
    menus = de.getMenu('IT계열')
    # menus2 = de.getMenu('2')
    print(menus)
    list = de.labeling(labels,menus)
    # list2 = de.labeling(labels, menus2)
    
    train_data,train_label = de.makeDataSets(list)
    # train_data2,train_label2 = de.makeDataSets(list2)
    
    train_data_n = np.array(train_data)/(len(labels)-1)
    train_label_n = np.array(train_label)
    
    # train_data_n2 = np.array(train_data2)/(len(labels)-1)
    # train_label_n2 = np.array(train_label2)
    
    np.save("train_data",train_data_n)
    np.save("train_label",train_label_n)
    
    # np.save("train_data2",train_data_n2)
    # np.save("train_label2",train_label_n2)
    
    print("labels",labels)
    print("menus",menus)
    print("list",list)
    print("train_data",train_data)
    print("train_label",train_label)
    
    print("train_data_n",train_data_n)
    print("train_label_n",train_label_n)