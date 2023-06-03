
import sqlite3 as sq


def get_bbs_counts():
    conn = sq.connect('./static/db/project.db')
    cur = conn.cursor()

    sql = 'select count(*) from bbs'
    cur.execute(sql)
    row = cur.fetchone()

    cur.close()
    conn.close()

    return row[0]


def get_bbs_list():
    conn = sq.connect('./static/db/project.db')
    cur = conn.cursor()

    sql = 'select bid, uid, title, name, date, review, reply from bbs'
    cur.execute(sql)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

def get_bbs_content(bid):
    conn = sq.connect('./static/db/project.db')
    cur = conn.cursor()

    sql = 'select * from bbs where bid = ?;'
    cur.execute(sql, (bid, ))
    row = cur.fetchone()

    cur.close()
    conn.close()

    return row