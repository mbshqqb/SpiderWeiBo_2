# -*- coding:utf-8 -*-
import gzip
from bs4 import BeautifulSoup
import json
import datetime
from com.zj.opener_com_file import *
from com.zj.get_weibo_detail_file import get_weibo_detail
def main():
    url = "http://d.weibo.com/"
    response = opener.open(url)
    print(response.info().get('Content-Encoding'))  # 获得编码，为gzip
    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    script=soup.find_all("script")[-1]
    json_str=script.text[8:-1]
    result=json.loads(json_str)
    content=result['html']

    content_soup = BeautifulSoup(content, 'html.parser')
    for url in content_soup.find_all(class_="WB_from S_txt2"):
        userid_weiboid = url.find("a")["href"].split("//weibo.com/")[1].split("/")
        print(userid_weiboid)
        user_id = userid_weiboid[0]
        weibo_id = userid_weiboid[1]
        get_weibo_detail(weibo_id, user_id, datetime.datetime.now()- datetime.timedelta(hours=50),"shehui_weibo_info")
main()

































