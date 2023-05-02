from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:   # method가 POST
        return '환영합니다.'

@app.route('/static_resource')
def static_resource():
    # static resource가 Cache로 인해서 즉시 변경이 일어나지 않을 경우
    image_file = os.path.join(app.root_path, 'static/img/dog1.jpg')
    mtime = int(os.stat(image_file).st_mtime)   # 마지막으로 변경된 시간
    return render_template('05.static.html', mtime=mtime)

if __name__ == '__main__':
    app.run(debug=True)