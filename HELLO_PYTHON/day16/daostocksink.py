import pymysql
import numpy as np

class DaoStockSink:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='_stock_old', charset='utf8')
 
        self.curs = self.conn.cursor()

    def selects(self):
        sql = f"""
            select * from stock_sync_0121
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        #print(rows)     # ( 가격 , ?)  리스트 []는 그 값의 생성, 삭제, 수정이 가능하지만 튜플 ()은 그 값을 바꿀 수 없다.
        
        row_c = []
        for r in rows :
            len_r = len(r)
            row_c.append(r[:len_r-1])
        
        
        rows_n = np.array(row_c)
        rows_t = np.transpose(rows_n)
        return rows_t


    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        
        
if __name__ == '__main__':
    dss = DaoStockSink()
    list = dss.selects()
    print("len",len(list))    # 총갯수 출력
    for idx,tu in enumerate(list):
        print(idx,tu)
    
    
    
    
    