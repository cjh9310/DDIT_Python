from flask import Flask
from flask.globals import request
from flask.templating import render_template
from flask.json import jsonify

app = Flask(__name__,static_url_path='')

@app.route('/')
def test():
    return render_template('test.html')

@app.route('/ajax', methods=['POST'])
def ajaxmod():
    stone = request.form['stone']
    data400 = request.form['data400']
    print("stone",stone)
    print("data400",data400)
    return jsonify({'i':0,'j':1})


if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")
    