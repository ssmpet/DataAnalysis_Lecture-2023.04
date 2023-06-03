from flask import Blueprint, request, render_template, session 
from flask import redirect, flash
import hashlib, base64, json
from user_util import get_weather
from db_sqlite import user_dao
import time
from datetime import datetime

user_bp = Blueprint('user_bp', __name__)
global g_quote
global g_quotes 
global g_addr
global g_weathers

@user_bp.route('/login', methods=['GET', 'POST'])    #localhost:5000/user/login이 처리되는 곳
def login():
    if request.method == 'GET':
        if 'quote' in session.keys(): quote = session['quote']
        if 'addr' in session.keys(): addr = session['addr']
        if 'weathers' in session.keys(): weathers = session['weathers']
        
        return render_template('prototype/user/login.html', menu=None, weather=get_weather(user_bp), quote=quote, addr=addr, weathers=weathers)
    else:

        uid = request.form['uid']
        pwd = request.form['pwd']

        # with open('static/data/password.txt') as f:
        #     s = f.read()
        # passwords = json.loads(s)

        user_info = user_dao.get_user(uid)
        if user_info :
        
            db_pwd = user_info[2]

            pwd_sha256 = hashlib.sha256(pwd.encode())
            hased_pwd = base64.b64encode(pwd_sha256.digest()).decode('utf-8')

            if hased_pwd == db_pwd:     
                flash(f'{user_info[1]}님 환영합니다.', category="info")   # 초기 화면으로 보내줌
                session['uid'] = uid                   # 세션값을 설정함으로써 사용자가 로그인하였음을 알게 함
                session['uname'] = user_info[1]
                session['email'] = user_info[3]
                return redirect('/home')
            else:
                flash('비밀번호가 틀립니다.', category="error")   # 로그인 화면을 다시 보내줌
                return redirect('/user/login')

        else:
            flash('가입되어 있지 않은 사용자 ID입니다. 회원가입을 해 주세요.', category="info")    # 회원 가입 페이지로 안내 or 다시 로그인
            return redirect('/user/register')

@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'quote' in session.keys(): quote = session['quote']
    if 'addr' in session.keys(): addr = session['addr']
    if 'weathers' in session.keys(): weathers = session['weathers']

    if request.method == 'GET':
        return render_template('prototype/user/register.html', menu=None, weather=get_weather(user_bp), quote=quote, addr=addr, weathers=weathers)
   
    else:
        uid = request.form['uid']

        if user_dao.get_user(uid) :
            flash('이미 사용자 ID가 있습니다. 다른 ID를 이용하세요.')
            return redirect('/user/register')
        
        pwd = request.form['pwd']
        pwd2 = request.form['pwd2']
        if pwd != pwd2 :
            flash('패스워드가 일치하지 않습니다.')
            return redirect('/user/register')
        uname = request.form['uname']
        uemail = request.form['email']

        pwd_sha256 = hashlib.sha256(pwd.encode())
        hased_pwd = base64.b64encode(pwd_sha256.digest()).decode('utf-8')
        udate = datetime.now()
        udate = udate.strftime('%Y-%m-%d %H:%M:%S')

        # print(uid, uname, hased_pwd, udate, uemail)
        user_dao.insert_user((uid, uname, hased_pwd, uemail, udate))

        session['uid'] = uid
        session['uname'] = uname
        session['email'] = uemail

        return redirect('/home')

@user_bp.route('/user_update', methods=['GET', 'POST'])
def user_update():
    
    if 'quote' in session.keys(): quote = session['quote']
    if 'addr' in session.keys(): addr = session['addr']
    if 'weathers' in session.keys(): weathers = session['weathers']

    if request.method == 'GET':
        return render_template('prototype/user/user_update.html', menu=None, weather=get_weather(user_bp), quote=quote, addr=addr, weathers=weathers)
    else:

        pwd = request.form['pwd']
        pwd2 = request.form['pwd2']
        if pwd != pwd2 :
            flash('패스워드가 일치하지 않습니다.')
            return redirect('/user/user_edit')
        
        uname = request.form['uname']
        uemail = request.form['email']

        pwd_sha256 = hashlib.sha256(pwd.encode())
        hased_pwd = base64.b64encode(pwd_sha256.digest()).decode('utf-8')
        user_dao.update_user((uname, hased_pwd, uemail, session['uid']))

        session['uname'] = uname
        session['email'] = uemail

        return redirect('/home')


@user_bp.route('/user_delete/<uid>')
def user_delete(uid):
    user_dao.delete_user(uid)
    session.pop('uid', None) 
    session.pop('uname', None)
    session.pop('email', None)
    return redirect('/home')


@user_bp.route('/logout')
def logout():
    session.pop('uid', None) 
    session.pop('uname', None)
    session.pop('email', None)

    return redirect('/home')