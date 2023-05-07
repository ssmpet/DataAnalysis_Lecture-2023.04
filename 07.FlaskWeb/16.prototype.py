from flask import Flask, render_template, request, url_for
from weather_util import get_weather
import interpark_util, genie_util, siksin_util

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/home')
def home():
    menu = {'ho': 1, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app))


@app.route('/user')
def user():
    menu = {'ho': 0, 'us': 1, 'cr': 0, 'ai': 0, 'sc': 0}
    return render_template('prototype/user.html', menu=menu, weather=get_weather(app))


@app.route('/interpark')
def interparkbest():

    book_rank = interpark_util.interpark_util()
    
    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    return render_template('prototype/interpark.html', menu=menu, weather=get_weather(app), book_rank=book_rank)

@app.route('/geniechart')
def geniechart():

    charts = genie_util.get_genie_chart()
    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    return render_template('prototype/geniechart.html', menu=menu, weather=get_weather(app), charts=charts)


@app.route('/siksin', methods=['GET', 'POST'])
def siksin():

    
    menu = {'ho': 0, 'us': 0, 'cr': 1, 'ai': 0, 'sc': 0}
    if request.method == 'GET':
        return render_template('prototype/siksin.html', menu=menu, weater=get_weather(app))
    else:
        place = request.form['place']
        siksins = siksin_util.get_siksin_util(place)
        return render_template('prototype/siksin_res.html', menu=menu, weater=get_weather(app), siksins=siksins)

@app.route('/schedule')
def schedule():
    menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 1}
    return render_template('prototype/schedule.html', menu=menu,  weather=get_weather(app))



if __name__ == '__main__':
    app.run(debug=True)