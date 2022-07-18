import pymysql

class DaoStock:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')
 
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selects(self,s_name):
        ret = []
        sql = f"""
            select s_code,ymd,s_name,price from stock
            where
            s_name = '{s_name}'
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for r in rows:
            ret.append(r['price'])
        return ret


    def getAllNames(self):
        ret = []
        sql = f"""
            SELECT s_name from stock
            GROUP BY s_name
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for r in rows:
            ret.append(r['s_name'])
        return ret
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoStock()
    list = de.getAllNames()
    for idx,i in enumerate(list):
        print(idx,i)
    
    
    
    
    