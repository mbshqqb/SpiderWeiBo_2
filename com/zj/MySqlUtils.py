# -*- coding:utf-8 -*-
import numpy as np

import pymysql
import csv
'''
user_info
weibo_info
comment_info
'''

def save_user(user_id, nick_name,user_gender,user_addr,weibo_number,flower_number,fans_number):
    conn = pymysql.connect(user='root', passwd='mbshqqb', host='172.17.11.173', db='weibo',charset="utf8")
    cur = conn.cursor()
    sql="insert into user_info(user_id, nick_name,user_gender,user_addr,weibo_number,flower_number,fans_number) values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,list([user_id, nick_name,user_gender,user_addr,weibo_number,flower_number,fans_number]))
    conn.commit()
    cur.close()
    conn.close()
def save_weibo(weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number):
    print(weibo_id,weibo_time)
    conn = pymysql.connect(user='root', passwd='mbshqqb', host='172.17.11.173', db='weibo',charset="utf8")
    cur = conn.cursor()
    sql="insert into weibo_info(weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number) values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(sql,list([weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number]))
    conn.commit()
    cur.close()
    conn.close()
def save_comment(weibo_id,comment_content,comment_thumbup_number):
    conn = pymysql.connect(user='root', passwd='mbshqqb', host='172.17.11.173', db='weibo',charset="utf8")
    cur = conn.cursor()
    sql="insert into comment_info(weibo_id,comment_content,comment_thumbup_number) values(%s,%s,%s)"
    cur.execute(sql,list([weibo_id,comment_content,comment_thumbup_number]))
    conn.commit()
    cur.close()
    conn.close()
def get_user_id():
    with open('用户id.csv') as f:
        reader=csv.reader(f)
        return [row[0] for row in reader]

def test():
    conn = pymysql.connect(user='root', passwd='mbshqqb', host='172.17.11.173', db='weibo',charset="utf8")
    cur = conn.cursor()
    sql = "select * from user_info"
    cur.execute(sql)
    result=cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()
test()
