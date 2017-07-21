# -*- coding:utf-8 -*-
import csv
import io
import numpy as np

import gzip
import re
import http.cookiejar
import urllib.parse
from bs4 import BeautifulSoup
from functools import reduce

from com.zj.MySqlUtils import *

user_ids=get_user_id()
domain_name='https://weibo.cn/'
headers=[('Host','weibo.cn'),
         ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'),
         ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
         ('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
         ('Accept-Encoding','gzip, deflate,br'),
         ('Cookie','_T_WM=b0e98dafcfb81283dd8bd10bd295dd5f; SUB=_2A250dSBDDeRhGeBN6lsQ8CbEzD-IHXVXlkALrDV6PUJbkdBeLRfFkW15tTVgK2mYmkEhiu2futd_rf8iHg..; SUHB=0rr7P_LK0D09f5; SCF=AiqzR4H6UsdurUY39t440i8siSE__ohFn_aCTbfASUVnRX4YznKw8y3nVdAxEoa9MoRbhSOwHuDQx5I2IspXrxw.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWYLj2OdBgHY.RWbiSN8cqN5JpX5oz75NHD95Qce024eK5R1hM0Ws4DqcjkK.HHPEH8SC-4eFHFSFH81FHWeE-4SCH81C-4eCHWBntt; SSOLoginState=1500598291; M_WEIBOCN_PARAMS=oid%3D4131701602404762%26featurecode%3D20000320%26luicode%3D10000011%26lfid%3D100803_ctg1_138_-_page_topics_ctg1__138'),
         ('Connection','keep-alive'),
         ('Upgrade-Insecure-Requests','1')
         ]
cj = http.cookiejar.CookieJar()
pro =urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)
opener.addheaders=headers

def get_weibo(weibo_id,user_id=None):
    weibo_url = domain_name + 'comment/' + weibo_id + "#cmtfrm"
    response = opener.open(weibo_url)
    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    #------------------------微博内容-----------------------------------
    user_id; weibo_content=None; weibo_time=''; forward_number=None; comment_number=None; thumbup_number=None;
    weibo_forwarding = soup.find(class_='c', id='M_').find(class_='cc')
    if weibo_forwarding is not None:#如果是转发的话
        user_id=soup.find(class_='c', id='M_').find(class_='cmt').find('a')['href'].split('/')[1]
        if user_id=='u':
            user_id=soup.find(class_='c', id='M_').find(class_='cmt').find('a')['href'].split('/')[2]
        weibo_id=weibo_forwarding['href'].split('/')[2].split('#')[0]
        get_weibo(weibo_id, user_id)
    else:#如果是原创
        weibo_content = soup.find(class_='c', id='M_').find(class_='ctt').text
        if weibo_content is None:#有多个content
            content_strs = [str for str in soup.find(class_='c', id='M_').find(class_='ctt').stripped_strings]
            weibo_content = reduce(lambda x, y: x + y, content_strs)
        weibo_time =soup.find(class_='c', id='M_').find(class_='ct').text
        #------微博数据--------只有原创有评论
        weibo_infos=[token for token in soup.find(id='cmtfrm').previous_sibling.stripped_strings]
        forward_number=weibo_infos[0]
        comment_number=weibo_infos[1]
        thumbup_number=weibo_infos[2]
        save_weibo(weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number)
        #------微博评论--------只有原创有评论
        comments=soup.find_all(id=re.compile("^C_\d*"),class_='c')
        for comment in comments:
            comment_content=comment.find(class_='ctt').text
            if comment_content is None:
                comment_contents = [str for str in comment.find(class_='ctt').stripped_strings]
                comment_content=reduce(lambda x,y:x+y,comment_contents).split(':')[-1]
            comment_thumbup_number=[str for str in comment.find(class_='cc').stripped_strings][0]
            save_comment(weibo_id,comment_content,comment_thumbup_number)

def get_user_weibos(user_id):
    url = domain_name + user_id
    response = opener.open(url)
    print(response.info().get('Content-Encoding'))  # 获得编码，为gzip
    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # ------------------------用户信息----------------------------
    # user_info
    user_info_soup = soup.find(class_='u').find(class_='ctt')
    user_infos = [token for token in user_info_soup.stripped_strings]
    nick_name = user_infos[0]
    user_gender = user_infos[1].split('/')[0]
    user_addr = user_infos[1].split('/')[1]
    # user_weibo_info
    weibo_number = soup.find(class_='u').find(class_='tip2').find(class_='tc').text
    flower_number =soup.find(class_='u').find(class_='tip2').find_all('a', recursive=False)[0].text
    fans_number =soup.find(class_='u').find(class_='tip2').find_all('a', recursive=False)[1].text

    save_user(user_id, nick_name,user_gender,user_addr,weibo_number,flower_number,fans_number)
    # ------------------------微博列表------------------------------------
    weibos = soup.find_all(class_='c', id=True)
    for weibo in weibos:
        weibo_id = weibo['id'].split('_')[1]
        get_weibo(weibo_id, user_id)

def main():
    for user_id in user_ids:
        get_user_weibos(user_id)
main()