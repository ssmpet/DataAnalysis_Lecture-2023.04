from flask import Flask, render_template, request
import map_util as mu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/hotplaces', methods=['GET', 'POST'])
def hotplaces():
    if request.method == 'GET':
        return render_template('10.수원hotplace.html')
    else:

        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']

        places = [place1, place2, place3]
        if mu.hot_places(places, app):
            return render_template('10.수원hotplace_res.html')
        else:
            return render_template('10.수원hotplace.html')


if __name__ == '__main__':
    app.run(debug=True)