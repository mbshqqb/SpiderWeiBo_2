# -*- coding:utf-8 -*-

import re
import datetime
strs=['90分钟前','今天 16:04','07月20日 15:26','2015-06-16 10:37:15']

def get_weibo_time(line):
    match_today = re.match(r'(\d{1,2})分钟前', line, re.M | re.I)
    if match_today:
        time=datetime.datetime.now().replace(microsecond=0)-datetime.timedelta(minutes=int(match_today.group(1)))
    else:
        match_minute = re.match(r'今天 (\d{2}):(\d{2})', line, re.M | re.I)
        if match_minute:
            time = datetime.datetime.now().replace(hour=int(match_minute.group(1)),minute=int(match_minute.group(2)),microsecond=0)
        else:
            match_year = re.match(r'(\d{1,2})月(\d{1,2})日 (\d{1,2}):(\d{1,2})', line, re.M | re.I)
            if match_year:
                time = datetime.datetime.now().replace(month=int(match_year.group(1)),day=int(match_year.group(2)),hour=int(match_year.group(3)),minute=int(match_year.group(4)),microsecond=0)
            else:
                match_standard = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})', line, re.M | re.I)
                if match_standard:
                    time=datetime.datetime.strptime(match_standard.group(1), '%Y-%m-%d %H:%M:%S')
                else:
                    print('!!!!!!!!!!!!',line)
    return time