# -*- coding:utf-8 -*-
import http.cookiejar
import urllib

domain_name='https://weibo.cn/'
headers=[('Host','weibo.cn'),
         ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'),
         ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
         ('Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'),
         ('Accept-Encoding','gzip, deflate,br'),
         ('Cookie','_T_WM=0fa19a062d6d0b2d6bcc92e582ba23ac; SUB=_2A250epzUDeRhGeNM7FYX9ivKyzuIHXVXhCScrDV6PUJbkdBeLRbAkW0vbVz5l3BmnBYjshd6mCXHOpcJLg..; SUHB=0XDl3fN4likDTk; SCF=Aj8H9NC6F-EONmVwL9k6wttmdkWeFz0Rexk5syRfb9CZrPMsItgVMHIjSlRcKhXOFNWXqT9QgY3BSkEPJYmte50.; SSOLoginState=1501490308'),
         ('Connection','keep-alive'),
         ('Upgrade-Insecure-Requests','1')
         ]
cj = http.cookiejar.CookieJar()
pro =urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)
opener.addheaders=headers