# -*- coding:utf-8 -*-
import csv

from com.zj.MDBUtils import *
def save_user(user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number):
    insert(['user_id',' nick_name','user_gender','user_addr','weibo_number','follower_number','fans_number'],[user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number],"user_info")

def save_weibo(table,weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number):
    insert(['weibo_id','user_id','weibo_content','weibo_time','forward_number','comment_number','thumbup_number'],[weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number],table)

def save_comment(weibo_id,comment_content,comment_thumbup_number):
    insert(['weibo_id','comment_content','comment_thumbup_number'],[weibo_id,comment_content,comment_thumbup_number],'comment_info')

# def get_user_id():
#     return ['alibuybuy']
def get_user_id():
    with open('用户id.csv') as f:
        reader=csv.reader(f)
        return [row[0] for row in reader]