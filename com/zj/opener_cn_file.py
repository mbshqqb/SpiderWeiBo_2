# -*- coding:utf-8 -*-
import http.cookiejar
import urllib

domain_name='https://weibo.cn/'
headers=[('Host','weibo.cn'),
         ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'),
         ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
         ('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
         ('Accept-Encoding','gzip, deflate,br'),
         ('Cookie','_T_WM=b0e98dafcfb81283dd8bd10bd295dd5f; SUB=_2A250dSBDDeRhGeBN6lsQ8CbEzD-IHXVXlkALrDV6PUJbkdBeLRfFkW15tTVgK2mYmkEhiu2futd_rf8iHg..; SUHB=0rr7P_LK0D09f5; SCF=AiqzR4H6UsdurUY39t440i8siSE__ohFn_aCTbfASUVnRX4YznKw8y3nVdAxEoa9MoRbhSOwHuDQx5I2IspXrxw.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWYLj2OdBgHY.RWbiSN8cqN5JpX5oz75NHD95Qce024eK5R1hM0Ws4DqcjkK.HHPEH8SC-4eFHFSFH81FHWeE-4SCH81C-4eCHWBntt; SSOLoginState=1500598291; M_WEIBOCN_PARAMS=oid%3D4131701602404762%26featurecode%3D20000320%26luicode%3D10000011%26lfid%3D100803_ctg1_138_-_page_topics_ctg1__138'),
         ('Connection','keep-alive'),
         ('Upgrade-Insecure-Requests','1')
         ]
cj = http.cookiejar.CookieJar()
pro =urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)
opener.addheaders=headers