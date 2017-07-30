# -*- coding:utf-8 -*-

# from com.zj.TESTDHelper import *
from com.zj.MDBHelper import get_weibo_ids
# from com.zj.MySQLDBHelper import *
import datetime

from com.zj.get_weibo_detail_file import get_weibo_detail


def main():
    for weibo_id,user_id in get_weibo_ids():
        get_weibo_detail(weibo_id, user_id,datetime.datetime.now()- datetime.timedelta(hours=100) , "weibo_info_2")
main()