from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/home')
def home():
    menu = {'ho': 1, 'us': 0, 'ai': 0, 'sc': 0}
    return render_template('prototype/home.html', menu=menu)

@app.route('/schedule')
def schedule():
    menu = {'ho': 0, 'us': 0, 'ai': 0, 'sc': 1}
    return render_template('prototype/schedule.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)