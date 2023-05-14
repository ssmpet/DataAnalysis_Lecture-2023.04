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
schedule_bp.static_folder = app.static_folder

# global quote, quotes   # 전역변수
# global g_addr
# global passwords

quotes = get_saying(app)
quote = random.sample(quotes, 1)[0]
print(quote)

# session 
# session['quotes'] = quotes
# session['quote'] = quote

# print(session['quote'])

g_addr = '수원시 장안구'

# session['addr'] = '수원시 장안구'
# print(session['addr'])

# global weathers
weathers = ''

###########################################
## 서버를 처음 실행시킬 때 한번 실행된다.


# with app.request_context(environ):
with app.test_request_context():
# def test_request():
    print('app_context')
    # global quote, quotes   # 전역변수
    # global g_addr
    # global passwords

    quotes = get_saying(app)
    quote = random.sample(quotes, 1)[0]

    # session 
    # session['quotes'] = quotes
    session['quote'] = quote

    # print(session['quote'])

    g_addr = '수원시 장안구'

    session['addr'] = '수원시 장안구'
    # print(session['addr'])

    # global weathers
    weathers = ''

# @app.before_request_funcs(test_request())
@app.route('/')
def index():
    print('index')
    

    return 'Hello Flask!!!'

# @app.route('/login')
# def login():
#     menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0, 'lo': 1}
#     return render_template('prototype/login.html', menu=menu, weather=get_weather(app), quote=quote, addr=g_addr, weathers=weathers)

@app.route('/home')
def home():

    print(session['quote'])
    print(session['addr'])

    menu = {'ho': 1, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app))

@app.route('/aboutme')
def aboutme():
    menu = {'ho': 0, 'us': 1, 'cr': 0, 'ai': 0, 'sc': 0}
    # return redirect('/schedule')
    return render_template('prototype/user.html', menu=menu, weather=get_weather(app), quote=quote, addr=g_addr, weathers=weathers)


@app.route('/interpark')
def interparkbest():

    book_rank = interpark_util.interpark_util()

    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    return render_template('prototype/interpark.html', menu=menu, weather=get_weather(app), book_rank=book_rank, quote=quote, addr=g_addr, weathers=weathers)

@app.route('/geniechart')
def geniechart():

    charts = genie_util.get_genie_chart()
    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    return render_template('prototype/geniechart.html', menu=menu, weather=get_weather(app), charts=charts, quote=quote, addr=g_addr, weathers=weathers)


@app.route('/genie_jquery')
def genie_jquery():

    charts = genie_util.get_genie_chart()
    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    return render_template('prototype/genie_jquery.html', menu=menu, weather=get_weather(app), charts=charts, quote=quote, addr=g_addr, weathers=weathers)


@app.route('/siksin', methods=['GET', 'POST'])
def siksin():

    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    if request.method == 'GET':
        return render_template('prototype/siksin.html', menu=menu, weater=get_weather(app), quote=quote, addr=g_addr, weathers=weathers)
    else:
        
        place = request.values['place']

        siksins = siksin_util.get_siksin_util(place)
        return siksins
        # return render_template('prototype/siksin_res.html', menu=menu, weater=get_weather(app), siksins=siksins, quote=quote, addr=g_addr, weathers=weathers)

@app.route('/siksin2')
def siksin2():
    
    # print('siksin2')
    # place = request.values['place']
    place = request.args.get('place')
    # print(place)
    siksins = siksin_util.get_siksin_util(place)
    return siksins        


###########################################
### for AJAX
###########################################
# 날씨 정보 가져오기 버튼 누를 때
@app.route('/get_weather')
def get_weath():
    area = request.args.get('addr') + '청'
    # global weathers
    weathers = get_weather(app, area)
    session['weathers'] = weathers
    return weathers
    # return jsonify(get_weather(app))

# 명언 수정
@app.route('/change_quote')
def change_quote():
    # global quote
    quote = random.sample(quotes, 1)[0]

    session['quote'] = quote

    return quote

@app.route('/change_addr')
def change_addr():
    # global g_addr
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
    app.run(debug=False)