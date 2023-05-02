from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):       # name 값을 주면 name은  그 값으로 되고, 안주면 None이 됨
    ex_dt = {'key1': 'value1', 'key2':'value2', 'key3': 'value3'}
    return render_template('06.hello.html', name=name, ex_dt=ex_dt, item='item')

if __name__ == '__main__':
    app.run(debug=True)