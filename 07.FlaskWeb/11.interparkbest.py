from flask import Flask, render_template
import interpark_util as mu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!!!'

@app.route('/interparkbest')
def interparkbest():

    book_rank = mu.interpark_util()

    return render_template('11.interparkbest.html', book_rank=book_rank)

if __name__ == '__main__':
    app.run(debug=True)