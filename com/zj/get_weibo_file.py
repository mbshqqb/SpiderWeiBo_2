# -*- coding:utf-8 -*-
import gzip
import re
import urllib.parse
from bs4 import BeautifulSoup
from functools import reduce
from com.zj.opener_cn_file import *
from com.zj.DBUtils import *
def get_weibo(weibo_id,user_id,table):
    try:
        weibo_url = domain_name + user_id + "/" + weibo_id
        response = opener.open(weibo_url)
    except urllib.error.URLError:
        try:
            weibo_url = domain_name +"comment/"+ weibo_id
            response = opener.open(weibo_url)
        except urllib.error.URLError:
            print(weibo_url)
            return

    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    #------------------------微博内容-----------------------------------
    user_id; weibo_content=None; weibo_time=''; forward_number=None; comment_number=None; thumbup_number=None;
    weibo_forwarding = soup.find(class_='c', id='M_').find(class_='cc')
    if weibo_forwarding is not None:#如果是转发的话
        print(weibo_id+":转发微博")
        user_id=soup.find(class_='c', id='M_').find(class_='cmt').find('a')['href'].split('/')[1]
        if user_id=='u':
            user_id=soup.find(class_='c', id='M_').find(class_='cmt').find('a')['href'].split('/')[2]
        weibo_id=weibo_forwarding['href'].split('/')[2].split('#')[0]
        get_weibo(weibo_id, user_id,table)
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
        save_weibo(table,weibo_id,user_id,weibo_content,weibo_time,forward_number,comment_number,thumbup_number)
        #------微博评论--------只有原创有评论
        comments=soup.find_all(id=re.compile("^C_\d*"),class_='c')
        for comment in comments:
            comment_content=comment.find(class_='ctt').text
            if comment_content is None:
                comment_contents = [str for str in comment.find(class_='ctt').stripped_strings]
                comment_content=reduce(lambda x,y:x+y,comment_contents).split(':')[-1]
            comment_thumbup_number=[str for str in comment.find(class_='cc').stripped_strings][0]
            save_comment(weibo_id,comment_content,comment_thumbup_number)
