# -*- coding:utf-8 -*-
#
# from com.zj.TESTDHelper import *
import datetime

from com.zj.MDBHelper import save_weibo_2, save_comment_2
# from com.zj.MySQLDBHelper import *
import gzip
import re
import urllib.parse
from bs4 import BeautifulSoup
from functools import reduce
from com.zj.opener_cn_file import opener
from com.zj.opener_cn_file import domain_name
def get_weibo_info(weibo_id, table):
    try:
        weibo_url = domain_name + "comment" + "/" + weibo_id
        response = opener.open(weibo_url)
    except urllib.error.URLError:
        print(weibo_url)
        return True

    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    #------------------------微博信息-----------------------------------
    forward_number=None; comment_number=None; thumbup_number=None;
    try:
        weibo_infos = [token for token in soup.find(id='cmtfrm').previous_sibling.stripped_strings]
        forward_number = weibo_infos[0]
        comment_number = weibo_infos[1]
        thumbup_number = weibo_infos[2]
        if save_weibo_2(table, weibo_id, forward_number, comment_number, thumbup_number) is False:
            return True
    except AttributeError:
        print("微博已经被删除")
        return True
    #------微博评论--------
    comments=soup.find_all(id=re.compile("^C_\d*"),class_='c')
    for comment in comments:
        comment_content=comment.find(class_='ctt').text
        if comment_content is None:
            comment_contents = [str for str in comment.find(class_='ctt').stripped_strings]
            comment_content=reduce(lambda x,y:x+y,comment_contents).split(':')[-1].strip()
        comment_thumbup_number=[str for str in comment.find(class_='cc').stripped_strings][0]
        save_comment_2(weibo_id,comment_content,comment_thumbup_number)
    return True