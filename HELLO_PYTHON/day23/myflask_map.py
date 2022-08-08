from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day09.daoemp import DaoEmp

app = Flask(__name__)


@app.route('/kakao')
def kakao():
    return render_template('map_kakao.html',list=list) 

@app.route('/')
@app.route('/naver')
def naver():
    return render_template('map_naver.html',list=list) 



 
if __name__ == '__main__':
    app.run(port=80)