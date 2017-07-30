# -*- coding:utf-8 -*-
import http.cookiejar
import urllib

domain_name='https://weibo.cn/'
headers=[('Host','weibo.cn'),
         ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'),
         ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
         ('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
         ('Accept-Encoding','gzip, deflate,br'),
         ('Cookie','_T_WM=e8c98a704f14a4db584c6cae7cd71b6e; SUB=_2A250eSBnDeRhGeNM7FYX9ivKyzuIHXVXgkAvrDV6PUJbkdBeLWnbkW1TWUNOVBQ373dYc2t_KqHMYRL7LQ..; SUHB=0V5lL7BvzM9vE7; SCF=Aj8H9NC6F-EONmVwL9k6wttmdkWeFz0Rexk5syRfb9CZwDmn_gO_t5jtnP5okmeyPWK2cNwDFBPkuOfUwa6WqFg.; SSOLoginState=1501384759'),
         ('Connection','keep-alive'),
         ('Upgrade-Insecure-Requests','1')
         ]
cj = http.cookiejar.CookieJar()
pro =urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)
opener.addheaders=headers