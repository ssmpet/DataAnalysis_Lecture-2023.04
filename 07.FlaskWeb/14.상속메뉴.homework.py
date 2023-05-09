from flask import Flask, render_template, request
import sub_util
import map_util
import interpark_util

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/main')
def main():
    return render_template('13.carousel.html', order=0)

@app.route('/scatter', methods=['GET', 'POST'])
def scatter():
    if request.method == 'GET':
        return render_template('09.산점도.html', order=1)
    else:
        print('산점도 POST')
        num = int(request.values['num'])
        xmean = int(request.values['mean'])
        xstd = int(request.values['std'])
        ymin = int(request.values['min'])
        ymax = int(request.values['max'])

        mtime = sub_util.sub_scatter(num, xmean, xstd, ymin, ymax, app)

        print(num, xmean, xstd, ymin, ymax, mtime)

        return str(mtime)
        # return render_template('09.산점도.html', order=1, mtime=mtime)
        # return render_template('09.산점도_res.html', order=1, mtime=mtime)



@app.route('/hotplaces', methods=['GET', 'POST'])
def hotplaces():
    if request.method == 'GET':
        return render_template('10.수원hotplace.html', order=2)
    else:

        print('hot place POST')
        place1 = request.values['place1']
        place2 = request.values['place2']
        place3 = request.values['place3']

        print(place1, place2, place3)

        places = [place1, place2, place3]

        map_util.hot_places(places, app)
        return 'OK'
        # if map_util.hot_places(places, app):
        #     return render_template('10.수원hotplace_res.html', order=2)
        # else:
        #     return render_template('10.수원hotplace.html', order=2)



@app.route('/interparkbest')
def interparkbest():

    book_rank = interpark_util.interpark_util()

    return render_template('11.interparkbest.html', book_rank=book_rank, order=3)

@app.route('/progress')
def progress():
    return render_template('13.progressbar.html', order=4)


if __name__ == '__main__':
    app.run(debug=True)