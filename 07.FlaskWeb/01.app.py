from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')

if __name__ == '__main__':
    app.run(debug=True)