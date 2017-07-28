# -*- coding:utf-8 -*-

import http.cookiejar
import urllib.parse

domain_name='https://d.weibo.com/'
headers=[('Host','d.weibo.cn'),
         ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'),
         ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
         ('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
         ('Accept-Encoding','gzip, deflate,br'),
         ('Cookie','_T_WM=451d135b896f5c5dfedca7eb2a8247d2; ALF=1503744173; SCF=AmBQspsc2kmw6gqq2d3An2jA3x-COEibtJsU9om4Nn71CFSJSxJXfAwoPiKTcySZKdCTeYdFyXmK8N_ZNBDklyk.; SUB=_2A250fbP-DeRhGeBN6lsQ8CbEzD-IHXVXgd22rDV6PUJbktBeLVXzkW1EskF00_OwJwwaCL1TuJN7I3e_MA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWYLj2OdBgHY.RWbiSN8cqN5JpX5o2p5NHD95Qce024eK5R1hM0Ws4DqcjkK.HHPEH8SC-4eFHFSFH81FHWeE-4SCH81C-4eCHWBntt; SUHB=0HTh8Oy8TD1jBB; SSOLoginState=1501152174'),
         ('Connection','keep-alive'),
         ('Upgrade-Insecure-Requests','1')
         ]
cj = http.cookiejar.CookieJar()
pro =urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)
opener.addheaders=headers