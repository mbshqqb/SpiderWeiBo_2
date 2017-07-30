# -*- coding:utf-8 -*-
# from com.zj.TESTDHelper import *
import datetime

from com.zj.MDBHelper import save_weibo, save_comment
# from com.zj.MySQLDBHelper import *
import gzip
import re
import urllib.parse
from bs4 import BeautifulSoup
from functools import reduce
from com.zj.opener_cn_file import opener
from com.zj.opener_cn_file import domain_name
from com.zj.get_weibo_time import get_weibo_time
from com.zj.get_user_weibos_file import get_user_weibos
def get_weibo_detail(weibo_id, user_id, time, table):
    try:
        weibo_url = domain_name + user_id + "/" + weibo_id
        response = opener.open(weibo_url)
    except urllib.error.URLError:
        try:
            weibo_url = domain_name +"comment/"+ weibo_id
            response = opener.open(weibo_url)
        except urllib.error.URLError:
            print(weibo_url)
            return True

    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    #------------------------微博内容-----------------------------------
    user_id; weibo_content=None; weibo_time=''; forward_number=None; comment_number=None; thumbup_number=None;

    try:
        weibo_forwarding = soup.find(class_='c', id='M_').find(class_='cc')
    except TypeError:
        print("TypeError:"+soup.find(class_='c', id='M_'))
        return True
    except AttributeError:
        print(weibo_id)
        print("AttributeError:" + soup.find(class_='c', id='M_'))
        return True
    is_original=True
    if weibo_forwarding is not None:#如果是转发的话
        is_original=False
        print(weibo_id+":转发微博")
        try:
            user_id = soup.find(class_='c', id='M_').find(class_='cmt').find('a')['href'].split('/')[1]
        except TypeError:
            print("TypeError:" , soup.find(class_='c', id='M_'))
            return True
        if user_id=='u':
            user_id=soup.find(class_='c', id='M_').find(class_='cmt').find('a')['href'].split('/')[2]

        weibo_id=weibo_forwarding['href'].split('/')[2].split('#')[0]
        if get_weibo_detail(weibo_id, user_id, time, table) is False:
            return False
        get_user_weibos(user_id, datetime.datetime.now().replace(year=2018), "")
    else:#如果是原创
        weibo_content = soup.find(class_='c', id='M_').find(class_='ctt')
        atags=weibo_content.find_all('a')
        for atag in atags:
            atag.extract()
        weibo_content=weibo_content.text.strip()
        weibo_time_str =soup.find(class_='c', id='M_').find(class_='ct').text.strip()

        weibo_time=get_weibo_time(weibo_time_str)

        if weibo_time<time:
            if is_original:
                return False
            else:
                return True
        #------微博数据--------只有原创有评论
        weibo_infos=[token for token in soup.find(id='cmtfrm').previous_sibling.stripped_strings]
        forward_number=weibo_infos[0]
        comment_number=weibo_infos[1]
        thumbup_number=weibo_infos[2]
        if save_weibo(table,weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number) is False:
            return True
        #------微博评论--------只有原创有评论
        comments=soup.find_all(id=re.compile("^C_\d*"),class_='c')
        for comment in comments:
            comment_content=comment.find(class_='ctt').text
            if comment_content is None:
                comment_contents = [str for str in comment.find(class_='ctt').stripped_strings]
                comment_content=reduce(lambda x,y:x+y,comment_contents).split(':')[-1].strip()
            comment_thumbup_number=[str for str in comment.find(class_='cc').stripped_strings][0]
            save_comment(weibo_id,comment_content,comment_thumbup_number)
    return True