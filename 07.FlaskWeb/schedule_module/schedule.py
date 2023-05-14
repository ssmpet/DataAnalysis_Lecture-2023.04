from flask import Blueprint, request, render_template, session, url_for
from flask import redirect, flash
from . import calendar_util as cu
from user_util import get_weather

schedule_bp = Blueprint('scheule_bp', __name__)

@schedule_bp.route('/schedule')
def schedule():    
    try : 
        tmp = session['uid']
    except:
        flash('스케줄을 확인하려면 로그인을 하여야 합니다.')
        return redirect('/user/login')

    menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 1}
    cals = cu.get_calendar(schedule_bp)
    return render_template('prototype/schedule/schedule.html', menu=menu, cals=cals)

