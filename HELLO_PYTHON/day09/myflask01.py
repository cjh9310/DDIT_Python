from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day09.daoemp import DaoEmp
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask'

@app.route('/para') # /para?a=555 입력
def para():
    a = request.args.get('a')
    return 'PARA'+a

@app.route('/post',methods=['GET','POST'])  # post + html의 value값
def post():
    a = request.form['a']
    return 'POST' +a 

@app.route('/dyna')
def dyna():
    a = "홍길동"
    b = ["홍길동","전우치","이순신"]
    c = [
        {"e_id" : '1',"e_name" : '1',"sex" : '1',"addr" : '1'},
        {"e_id" : '2',"e_name" : '2',"sex" : '2',"addr" : '2'}
    ]
    
    return render_template('dyna.html',a=a,b=b,c=c) 
    # dyna.html을 찾을 수 없다고 떠서 day09에 templates라는 폴더를 생성해 넣어줌


@app.route('/emp_list')
def emp_list():
    de = DaoEmp()
    list = de.selects()
    return render_template('emp_list.html',list=list) 

 
if __name__ == '__main__':
    app.run()