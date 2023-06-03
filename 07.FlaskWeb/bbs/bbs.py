from flask import Blueprint, request, render_template, session
from flask import redirect, flash

bbs_bp = Blueprint('bbs_bp', __name__)

@bbs_bp.route('/list')
def list():
    menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0, 'bb': 1}
    return render_template('prototype/bbs/list.html', menu=menu)