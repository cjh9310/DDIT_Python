import pymysql

class DaoEmp :
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='python',port=3305,
                       db='python', charset='utf8')

        self.curs = self.conn.cursor(pymysql.cursors.DictCursor) # self. == 전역변수
    
    def selects(self):
        sql = "select * from emp"
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows
    
    def select(self,e_id):
        sql = f""" 
            select e_id,e_name,sex,addr  
            from emp   
            where e_id = '{e_id}'
            """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        return rows[0]  
    # [0]없이 실행하면 배열과 결과값이 같이 나오는데
    # [0]을 넣으면 []가 제외되고 결과값만 나온다.
    
    def insert(self,e_name,sex,addr):
        sql = f"""
            insert into emp
            (e_name,sex,addr)
            values
            ('{e_name}','{sex}','{addr}')
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def update(self,e_id,e_name,sex,addr):
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
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
            delete from emp
            where
                e_id = '{e_id}'
            
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self) :
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.delete('6')
    print("cnt",cnt)        
    

