# -*- coding:utf-8 -*-

# from com.zj.TESTDHelper import *
# from com.zj.MDBHelper import *
from com.zj.MySQLDBHelper import *
import datetime

from com.zj.get_weibo_detail_file import get_weibo_detail


def main():
    for weibo_user in get_weibo_ids():
        get_weibo_detail(weibo_user[0], weibo_user[1],datetime.datetime.now()- datetime.timedelta(hours=60) , "weibo_info_2")
main()