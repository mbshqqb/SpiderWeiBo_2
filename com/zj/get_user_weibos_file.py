# -*- coding:utf-8 -*-
# from com.zj.TESTDHelper import *
from com.zj.MDBHelper import *
# from com.zj.MySQLDBHelper import *
from com.zj.get_page_weibo_file import *
def get_user_weibos(user_id,time,table):
    try:
        user_url = domain_name + user_id
        response = opener.open(user_url)
    except urllib.error.URLError:
        print(user_url)
        return True

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
    follower_number =soup.find(class_='u').find(class_='tip2').find_all('a', recursive=False)[0].text
    fans_number =soup.find(class_='u').find(class_='tip2').find_all('a', recursive=False)[1].text
    if save_user(user_id, nick_name,user_gender,user_addr,weibo_number,follower_number,fans_number) is False:
        return True

    #获得微博页数
    pages=[token for token in soup.find(class_="pa").stripped_strings][1][2:-1]
    # ------------------------微博列表------------------------------------
    #从第一页开始爬取
    for page in range(int(pages)):
        page=page+1
        print(page)
        if get_page_weibo(page,user_id,time,table) is False:
            return True
    return True