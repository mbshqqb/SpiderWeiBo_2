# -*- coding:utf-8 -*-

from com.zj.get_weibo_file import *
from com.zj.DBUtils import *
def get_user_weibos(user_id,table):
    url = domain_name + user_id
    response = opener.open(url)
    print(response.info().get('Content-Encoding'))  # 获得编码，为gzip
    data = response.read()
    # gzip解压
    html = gzip.decompress(data).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    # ------------------------用户信息----------------------------
    # user_info
    print(html)
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
        get_weibo(weibo_id, user_id,table)