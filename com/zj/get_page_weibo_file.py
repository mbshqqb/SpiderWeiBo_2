# -*- coding:utf-8 -*-
import gzip
import urllib

from bs4 import BeautifulSoup

from com.zj.get_weibo_detail_file import get_weibo_detail
from com.zj.opener_cn_file import domain_name, opener


def get_page_weibo(page,user_id,time,table):
    try:
        page_url = domain_name + user_id + '?page='+str(page)
        response = opener.open(page_url)
    except urllib.error.URLError:
        print(page_url)
        return True
    print(response.info().get('Content-Encoding'))  # 获得编码，为gzip
    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    weibos = soup.find_all(class_='c', id=True)
    for weibo in weibos:
        weibo_id = weibo['id'].split('_')[1]
        if get_weibo_detail(weibo_id, user_id, time, table) is False:
            return False
    return True