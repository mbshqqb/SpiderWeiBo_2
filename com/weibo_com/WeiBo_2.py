# -*- coding:utf-8 -*-

# from com.zj.TESTDHelper import *
from com.zj.MDBHelper import get_weibo_ids
from com.zj.MDBHelper import exist_weibo2_id
# from com.zj.MySQLDBHelper import *
import datetime

from com.zj.get_weibo_info_file import get_weibo_info


def main():
    for weibo_id in get_weibo_ids():
        if not exist_weibo2_id(weibo_id):
            get_weibo_info(weibo_id,"weibo_info_2")
main()