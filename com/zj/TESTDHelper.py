# -*- coding:utf-8 -*-
import csv


def save_user(user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number):
    #print(user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number)
    pass

def save_weibo(table,weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number):
    print(weibo_id,weibo_time)
    pass

def save_comment(weibo_id,comment_content,comment_thumbup_number):
    #print(weibo_id,comment_content,comment_thumbup_number)
    pass

def get_user_id():
    with open('用户id.csv') as f:
        reader=csv.reader(f)
        return [row[0] for row in reader]