import pymysql
import numpy as np

class DaoMenu:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def getGroupMenu(self):
        sql = f"""
                SELECT distinct menu 
                FROM menu
                order by menu
                """
        arr = []
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            arr.append(row['menu'])
        return arr


    def getMenu(self,e_id):
        sql = f"""
                SELECT *
                FROM menu
                WHERE
                    e_id = '{e_id}'
                ORDER BY ymd
                """
        arr = []
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        print(rows)
        arr = []
        for row in rows:
            arr.append(row['menu'])
        
        return arr
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
    menus = de.getMenu('1')
    # menus2 = de.getMenu('2')
    
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
    print(type(labels))
    print("labels",labels)
    print("menus",menus)
    print("list",list)
    print("train_data",train_data)
    print("train_label",train_label)
    
    print("train_data_n",train_data_n)
    print("train_label_n",train_label_n)