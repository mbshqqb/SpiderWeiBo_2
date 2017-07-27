# -*- coding:utf-8 -*-
import numpy as np
import csv
def save_comment(weibo_id,comment_content,comment_thumbup_number):
    comment_info_file = open('comment_info.csv', 'a', newline='',encoding='utf-8')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(comment_info_file)
    writer.writerow([weibo_id,comment_content,comment_thumbup_number])
    comment_info_file.close()

def save_weibo(user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number):
    weibo_info_file = open('weibo_info.csv', 'a', newline='',encoding='utf-8')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(weibo_info_file)
    writer.writerow([weibo_content,weibo_time,forward_number,comment_number,thumbup_number])
    weibo_info_file.close()

def save_user(user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number):
    user_info_file = open('user_info.csv', 'a', newline='',encoding='utf-8')  # 设置newline，否则两行之间会空一行
    writer = csv.writer(user_info_file)
    writer.writerow([user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number])
    user_info_file.close()