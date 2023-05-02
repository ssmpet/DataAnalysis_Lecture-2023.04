import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import os


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/scatter', methods=['GET', 'POST'])
def scatter():
    if request.method == 'GET':
        return render_template('09.산점도.html')
    else:
        num = int(request.form['num'])
        xmean = int(request.form['mean'])
        xstd = int(request.form['std'])
        ymin = int(request.form['min'])
        ymax = int(request.form['max'])
        
        xs = np.random.normal(loc=xmean, scale=xstd, size=num)
        ys = np.random.uniform(ymin, ymax, num)

        # figure 를 꼭 써 주어야 함. 새로운 객체 생성
        plt.figure()
        plt.scatter(xs, ys)
        filename = os.path.join(app.static_folder, 'img/scatter.png')
        plt.savefig(filename)
        return render_template('09.산점도_res.html')

if __name__ == '__main__':
    app.run(debug=True)