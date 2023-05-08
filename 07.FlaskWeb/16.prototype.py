from flask import Flask, render_template, request, url_for, jsonify
from user_util import get_weather, get_saying, chg_profile
import interpark_util, genie_util, siksin_util
import random, os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'


@app.route('/home')
def home():
    menu = {'ho': 1, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app), quote=quote, addr=g_addr, weathers=weathers)


@app.route('/user')
def user():
    menu = {'ho': 0, 'us': 1, 'cr': 0, 'ai': 0, 'sc': 0}
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


@app.route('/siksin', methods=['GET', 'POST'])
def siksin():
    
    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    if request.method == 'GET':
        return render_template('prototype/siksin.html', menu=menu, weater=get_weather(app), quote=quote, addr=g_addr, weathers=weathers)
    else:
        print('POST')
        # place = request.values['place']
        place = request.args.get('place')
        print(place)
        siksins = siksin_util.get_siksin_util(place)
        return siksins        
        # return render_template('prototype/siksin_res.html', menu=menu, weater=get_weather(app), siksins=siksins, quote=quote, addr=g_addr, weathers=weathers)

@app.route('/siksin2')
def siksin2():
    
    print('siksin2')
    # place = request.values['place']
    place = request.args.get('place')
    print(place)
    siksins = siksin_util.get_siksin_util(place)
    return siksins        

@app.route('/schedule')
def schedule():
    menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 1}
    return render_template('prototype/schedule.html', menu=menu,  weather=get_weather(app), quote=quote, addr=g_addr, weathers=weathers)

###########################################
### for AJAX
###########################################
# 날씨 정보 가져오기 버튼 누를 때
@app.route('/get_weather')
def get_weath():
    area = request.args.get('addr') + '청'
    global weathers
    weathers = get_weather(app, area)
    return weathers
    # return jsonify(get_weather(app))

# 명언 수정
@app.route('/change_quote')
def change_quote():
    global quote
    quote = random.sample(quotes, 1)[0]
    return quote

@app.route('/change_addr')
def change_addr():
    global g_addr
    g_addr = request.args.get('addr')
    return g_addr

@app.route('/change_profile', methods=['POST'])
def change_profile():
    file_image = request.files['image']
    filename = os.path.join(app.static_folder, f'upload/{file_image.filename}')

    file_image.save(filename)

    mtime = chg_profile(app, filename)
    return str(mtime)

###########################################
## 서버를 처음 실행시킬 때 한번 실행된다.
with app.app_context():
    print('app_context')
    global quote, quotes   # 전역변수
    global g_addr
    quotes = get_saying(app)
    quote = random.sample(quotes, 1)[0]
    g_addr = '수원시 장안구'
    global weathers
    weathers = ''

if __name__ == '__main__':
    app.run(debug=True)