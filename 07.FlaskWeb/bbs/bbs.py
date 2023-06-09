from flask import Blueprint, request, render_template, session
from flask import redirect, flash
from db_sqlite import bbs_dao

bbs_bp = Blueprint('bbs_bp', __name__)

@bbs_bp.route('/list/<int:page_no>')
def list(page_no):
    menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0, 'bb': 1}
    total = bbs_dao.get_bbs_total()
    # print('total = ', total, total//5)
    offset = (page_no - 1) * 10
    bbs_list = bbs_dao.get_bbs_list(offset)
    # page_no = int(page_no)
    start_page = ((page_no-1)//5 ) * 5 + 1
    total_page = total//5
    # total_page = total//10 if total%10==0 else total//10 + 1
    tmp = ((total_page-1)//5) * 5 + 1
    end_page = start_page+(total_page%5) if start_page == tmp else start_page + 4
    
    # print(page_no, start_page, end_page, total_page)

    return render_template('prototype/bbs/list.html', menu=menu, total_page=total_page, 
                           page_no=page_no, start_page=start_page, end_page=end_page,
                           bbs_list=bbs_list)


@bbs_bp.route('/view/<int:bid>')
def list_view(bid):
    menu = {'ho': 0, 'us': 0, 'cr': 0, 'ai': 0, 'sc': 0, 'bb': 1}

    contents = bbs_dao.get_bbs_content(bid)
    return render_template('prototype/bbs/view.html', menu=menu, contents=contents)