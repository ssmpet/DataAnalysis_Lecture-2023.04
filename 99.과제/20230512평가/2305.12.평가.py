from flask import Flask, render_template
import melon_util as mu
import youtube_rank_util as yu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/melon')
def melon():

    charts = mu.melon_util()
    return render_template('melon.html', charts=charts)

@app.route('/youtube_ranking')
def youtube_ranking():

    ranks = yu.youtube_rank_util()
    
    return render_template('youtube_ranking.html', ranks=ranks)

if __name__ == '__main__':
    app.run(debug=True)