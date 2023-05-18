from flask import Blueprint, request, render_template, session, url_for
from flask import redirect, flash
from . import calendar_util as cu
from user_util import get_weather

schedule_bp = Blueprint('scheule_bp', __name__)

@schedule_bp.route('/schedule', methods=['GET', 'POST'])
def schedule():    
    try : 
        tmp = session['uid']
    except:
        flash('스케줄을 확인하려면 로그인을 하여야 합니다.')
        return redirect('/user/login')

    if 'quote' in session.keys(): quote = session['quote']
    if 'addr' in session.keys(): addr = session['addr']
    if 'weathers' in session.keys(): weathers = session['weathers']

    cday = ''
    try:
        cday = request.values['today']
    except:
        pass

    if request.method == 'GET':
        menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 1}
        # cals = cu.get_calendar(schedule_bp, cday)
        return render_template('prototype/schedule/schedule.html', menu=menu, weather=get_weather(schedule_bp), quote=quote, addr=addr, weathers=weathers)
    else:
        # print('current_day ' + cday)
        cals = cu.get_calendar(schedule_bp, cday)
        # print(cals)
        return cals
        # return ''


