from flask import Flask, render_template, request
import melon_util as mu
import youtube_rank_util as yu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/melon')
def melon():

    charts = mu.melon_util()
    return render_template('melon.html', charts=charts, order=0)

@app.route('/pleas_wait')
def pleas_wait():

    return render_template('pleas_wait.html', order=1)


@app.route('/youtube_ranking', methods=['GET', 'POST'])
def youtube_ranking():

    if request.method == 'GET':
        ranks = yu.youtube_rank_util(app)
        return render_template('youtube_ranking.html', ranks=ranks, order=1)
    else:
        rank = request.values['rank']
        if rank == 'top20':
            return str(yu.rank_top20(app))
        else:
            return str(yu.rank_top10(app))
        
if __name__ == '__main__':
    app.run(debug=True)