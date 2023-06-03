from flask import Blueprint, request, render_template, session
from flask import redirect, flash
from db_sqlite import bbs_dao

bbs_bp = Blueprint('bbs_bp', __name__)

@bbs_bp.route('/list')
def list():
    menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0, 'bb': 1}
    bbs_count = bbs_dao.get_bbs_counts()
    bbs_list = bbs_dao.get_bbs_list()

    return render_template('prototype/bbs/list.html', menu=menu, bbs_count=bbs_count, bbs_list=bbs_list)