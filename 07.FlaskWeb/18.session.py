from flask import Flask, render_template, request, url_for, jsonify, redirect, session, flash
from user_util import get_weather, get_saying, chg_profile
import interpark_util, genie_util, siksin_util
import random, os, json
from user_module.user import user_bp
from schedule_module.schedule import schedule_bp

app = Flask(__name__)
app.secret_key = 'qwert12345'
app.config['SESSION_COOKIE_PATH'] = '/'


app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(schedule_bp, url_prefix='/schedule')
user_bp.static_folder = app.static_folder
schedule_bp.static_folder = app.static_folder

###########################################
## 서버를 처음 실행시킬 때 한번 실행된다.

with app.test_request_context():

    print('app_context')
    global g_quote
    global g_quotes   # 전역변수
    global g_addr
    global g_weathers

    g_quotes = get_saying(app)
    g_quote = random.sample(g_quotes, 1)[0]
    g_addr = '수원시 장안구'
    g_weathers = ''
   
# @app.before_request_funcs(test_request())
@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/home')
def home():

    if 'quote' not in session.keys() : session['quote'] = g_quote
    if 'addr' not in session.keys() : session['addr'] = g_addr
    if 'weathers' not in session.keys() : session['weathers'] = g_weathers

    menu = {'ho': 1, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app), quote=g_quote, addr=g_addr, weathers=g_weathers)

@app.route('/aboutme')
def aboutme():
    menu = {'ho': 0, 'us': 1, 'cr': 0, 'ai': 0, 'sc': 0}
    # print(g_quote)
    return render_template('prototype/user.html', menu=menu, weather=get_weather(app), quote=g_quote, addr=g_addr, weathers=g_weathers)


@app.route('/interpark')
def interparkbest():

    book_rank = interpark_util.interpark_util()

    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    return render_template('prototype/interpark.html', menu=menu, weather=get_weather(app), book_rank=book_rank, quote=g_quote, addr=g_addr, weathers=g_weathers)

@app.route('/geniechart')
def geniechart():

    charts = genie_util.get_genie_chart()
    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    return render_template('prototype/geniechart.html', menu=menu, weather=get_weather(app), charts=charts, quote=g_quote, addr=g_addr, weathers=g_weathers)


@app.route('/genie_jquery')
def genie_jquery():

    charts = genie_util.get_genie_chart()
    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    return render_template('prototype/genie_jquery.html', menu=menu, weather=get_weather(app), charts=charts, quote=g_quote, addr=g_addr, weathers=g_weathers)


@app.route('/siksin', methods=['GET', 'POST'])
def siksin():

    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    if request.method == 'GET':
        return render_template('prototype/siksin.html', menu=menu, weater=get_weather(app), quote=g_quote, addr=g_addr, weathers=g_weathers)
    else:
        
        place = request.values['place']

        siksins = siksin_util.get_siksin_util(place)
        # print(siksins)
        return siksins


###########################################
### for AJAX
###########################################
# 날씨 정보 가져오기 버튼 누를 때
@app.route('/get_weather')
def get_weath():
    area = request.args.get('addr') + '청'
    global g_weathers
    g_weathers = get_weather(app, area)
    session['weathers'] = g_weathers
    return g_weathers
    # return jsonify(get_weather(app))

# 명언 수정
@app.route('/change_quote')
def change_quote():
    global g_quote
    g_quote = random.sample(g_quotes, 1)[0]
    session['quote'] = g_quote
    return g_quote

@app.route('/change_addr')
def change_addr():
    global g_addr
    g_addr = request.args.get('addr')
    session['addr'] = g_addr
    return g_addr

@app.route('/change_profile', methods=['POST'])
def change_profile():
    file_image = request.files['image']
    filename = os.path.join(app.static_folder, f'upload/{file_image.filename}')

    file_image.save(filename)

    mtime = chg_profile(app, filename)
    return str(mtime)



if __name__ == '__main__':
    try:
        app.run(debug=False)
    finally:
        print('main end')