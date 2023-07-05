# World database의 song, girl_group를 액세스 하는 라이브러리
# Connection Pool 사용
# 설치: pip install mysql-connector-python


import pymysql
import json
from mysql.connector import pooling

with open('./mysql.json') as f:
    config_str = f.read()

config = json.loads(config_str)
pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=3, **config)

def get_song_list_by_debut(year):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()
    cur = conn.cursor()
    # like 문 주의 %가 들어가는 구문은 CONCAT으로 붙여주어서 찾는다.
    # sql = "SELECT * FROM girl_group WHERE debut LIKE CONCAT(%s, '%%') ORDER BY debut"
    sql = "SELECT * FROM girl_group WHERE debut BETWEEN %s AND %s ORDER BY debut"
    cur.execute(sql, (year+"-01-01", year+"-12-31"))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_song_list(num, offset=0):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM song LIMIT %s OFFSET %s;"
    cur.execute(sql, (num, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def get_girl_group_list(num, offset=0):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "SELECT * FROM girl_group ORDER BY debut LIMIT %s OFFSET %s;"
    cur.execute(sql, (num, offset))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows


def insert_song(params):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO song VALUES(DEFAULT, %s, %s);"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()


def insert_girl_group(params):
    # conn = pymysql.connect(**config)
    conn = pool.get_connection()
    cur = conn.cursor()
    sql = "INSERT INTO girl_group VALUES(DEFAULT, %s, %s, %s);"
    cur.execute(sql, params)
    conn.commit()
    cur.close()
    conn.close()

