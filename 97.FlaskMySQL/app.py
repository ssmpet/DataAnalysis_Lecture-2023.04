from flask import Flask, render_template, request, redirect
import db.kpop_dao as kd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/song/list')
def song_list():
    songs = kd.get_song_list(25)
    return render_template('01.song_list.html', songs=songs)


@app.route('/song/insert', methods=['GET', 'POST'])
def song_insert():

    if request.method == 'GET':
        return render_template('02.song_insert.html')
    else:
        title = request.form['title']
        lyrics = request.form['lyrics']
        kd.insert_song((title, lyrics))
        return redirect('/song/list')
    
@app.route('/song/update/<sid>', methods=['GET', 'POST'])
def song_update(sid):

    if request.method == 'GET':
        song = kd.get_song(sid)
        return render_template('03.song_update.html', song=song)
    else:
        title = request.form['title']
        lyrics = request.form['lyrics']
        kd.update_song((title, lyrics, sid))
        return redirect('/song/list')
    
@app.route('/song/delete/<sid>', methods=['GET', 'POST'])
def song_delete(sid):

    if request.method == 'GET':
        kd.delete_song(sid)
        return redirect('/song/list')

   

@app.route('/gg/list')
def gg_list():
    groups = kd.get_girl_group_list(25)
    return render_template('11.gg_list.html', groups=groups)


@app.route('/gg/insert', methods=['GET', 'POST'])
def gg_insert():
    if request.method == 'GET':
        return render_template('12.gg_insert.html')
    else:

        name = request.form['name']
        debut = request.form['debut']
        hit_song_id = request.form['hit_song_id']
        kd.insert_girl_group((name, debut, hit_song_id))
        return redirect('/gg/list')
    

@app.route('/gg/update/<gid>', methods=['GET', 'POST'])
def gg_update(gid):

    if request.method == 'GET':
        group = kd.get_gg(gid)
        return render_template('13.gg_update.html', group=group)
    else:
        name = request.form['name']
        debut = request.form['debut']
        hit_song_id = request.form['hit_song_id']
        kd.update_gg((name, debut, hit_song_id, gid))
        return redirect('/gg/list')
    
@app.route('/gg/delete/<gid>', methods=['GET', 'POST'])
def gg_delete(gid):

    if request.method == 'GET':
        kd.delete_gg(gid)
        return redirect('/gg/list')
    

if __name__ == '__main__':
    app.run(debug=True)
