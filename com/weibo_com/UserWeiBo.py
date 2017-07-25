# -*- coding:utf-8 -*-

from com.zj.DBUtils import *
from com.zj.get_user_weibos_file import get_user_weibos
user_ids=get_user_id()

def main():
    for user_id in user_ids:
        get_user_weibos(user_id,"weibo_info")
main()