# -*- coding:utf-8 -*-
# from com.zj.TESTDHelper import *
import gzip
import urllib

from bs4 import BeautifulSoup

from com.zj.MDBHelper import exist_user_id, save_user
# from com.zj.MySQLDBHelper import *
from com.zj.opener_cn_file import domain_name, opener


def get_user_weibos(user_id,time,table):
    from com.zj.get_page_weibo_file import get_page_weibo
    if exist_user_id(user_id):
        return True
    try:
        user_url = domain_name + user_id
        response = opener.open(user_url)
    except urllib.error.URLError:
        print(user_url)
        return True
    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # ------------------------用户信息----------------------------
    # user_info
    print("user_start:",user_id)
    print(html)
    user_info_soup = soup.find(class_='u').find(class_='ctt')
    user_infos = [token for token in user_info_soup.stripped_strings]
    try:
        nick_name = user_infos[0]
        user_gender = user_infos[1].split('/')[0]
        user_addr = user_infos[1].split('/')[1]
    except IndexError:
        return True
    # user_weibo_info
    weibo_number = soup.find(class_='u').find(class_='tip2').find(class_='tc').text
    follower_number =soup.find(class_='u').find(class_='tip2').find_all('a', recursive=False)[0].text
    fans_number =soup.find(class_='u').find(class_='tip2').find_all('a', recursive=False)[1].text

    #获得微博页数
    pages=[token for token in soup.find(class_="pa").stripped_strings][1][2:-1]
    # ------------------------微博列表------------------------------------
    #从第一页开始爬取,爬取完所有的页之后需要保存用户
    for page in range(int(pages)):
        page=page+1
        print('page:',page)
        if get_page_weibo(page,user_id,time,table) is False:
            save_user(user_id, nick_name, user_gender, user_addr, weibo_number, follower_number, fans_number)
            print("user_end",user_id)
            return True
    return True