# -*- coding:utf-8 -*-
import csv

import datetime

from com.zj.MDBUtils import *

def save_user(user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number):
    print('user:',user_id)
    if insert(['user_id',' nick_name','user_gender','user_addr','weibo_number','follower_number','fans_number'],
              [user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number],"user_info") is False:
        return False
    return True

def save_weibo(table,weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number):
    print(weibo_id,weibo_time)
    if insert(['weibo_id','user_id','weibo_content','weibo_time','forward_number','comment_number','thumbup_number'],
              [weibo_id,user_id,weibo_content, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),forward_number,comment_number,thumbup_number],table)is False:
        return False
    return True

def save_comment(weibo_id,comment_content,comment_thumbup_number):
    insert(['weibo_id','comment_content','comment_thumbup_number'],[weibo_id,comment_content,comment_thumbup_number],'comment_info')

def exist_user_id(user_id):
    rows=get('user_info','user_id',user_id)
    if len(rows)==0:
        return False
    else:
        return True


#     return ['alibuybuy']
def get_user_id():
    with open('id_12.csv') as f:
        reader=csv.reader(f)
        return [row[0] for row in reader]

def get_weibo_ids():
    list=get_all("weibo_info","weibo_id","user_id")
    for k_v in list:
        yield k_v.get("weibo_id"),k_v.get("user_id")
