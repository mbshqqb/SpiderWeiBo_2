# -*- coding:utf-8 -*-

# from com.zj.TESTDHelper import *
from com.zj.MDBHelper import get_user_id
from com.zj.get_user_weibos_file import get_user_weibos
import datetime

user_ids=get_user_id()
def main():
    for user_id in user_ids:
        if get_user_weibos(user_id,datetime.datetime.now()- datetime.timedelta(hours=50),"weibo_info") is False:
            break
main()