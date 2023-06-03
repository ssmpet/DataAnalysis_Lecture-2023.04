
#
# user(사용자) table에 대한 Data Access Object(DAO)
#
import sqlite3 as sq

def get_user(uid):
    conn = sq.connect('./static/db/project.db')
    cur = conn.cursor()

    sql = 'select * from user where uid=?;'
    cur.execute(sql, (uid, ))
    row = cur.fetchone()
    
    cur.close()
    conn.close()

    return row 

def insert_user(params):
    print('step1')

    conn = sq.connect('./static/db/project.db')
    print('step2')
    cur = conn.cursor()
    print('step3')
    sql = 'insert into user values (?, ?, ?, ?, ?);'
    cur.execute(sql, params)
    conn.commit()

    cur.close()
    conn.close()

def update_user(params):
    conn = sq.connect('./static/db/project.db')
    cur = conn.cursor()


    sql = 'update user set uname=?, upwd=?, uemail=? where uid=?;'
    cur.execute(sql, params)
    conn.commit()

    cur.close()
    conn.close()

def delete_user(uid):
    conn = sq.connect('./static/db/project.db')
    cur = conn.cursor()

    sql = 'delete from user where uid=?;'
    cur.execute(sql, (uid, ))
    conn.commit()

    cur.close()
    conn.close()

