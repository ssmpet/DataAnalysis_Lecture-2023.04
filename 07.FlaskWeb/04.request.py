from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')

# localhost:5000/area?pi=3.14&radius=5
@app.route('/area')     # 아무런 얘기가 없으면 GET 방식
def area():
    pi = request.args.get('pi', '3.14159') # default값을 줄수 있다.
    radius = request.values['radius']
    a = float(pi) * float(radius) ** 2
    return f'<h1>pi={pi}, radius={radius}, area={a}</h1>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:   # method가 POST
        uid = request.form['uid']
        pwd = request.values['pwd']

        return f'<h1>uid={uid}, pwd={pwd}</h1>'



if __name__ == '__main__':
    app.run(debug=True)