#!/usr/bin/python
# -*- coding:utf-8 -*-

import time


#判断时间
def timecheck(begin=0730,end=2350):
    xtime = int(time.strftime("%H%M", time.localtime()))
    if xtime >= begin and xtime < end:
        return 1
    else:
        time.sleep(60)
    return timecheck()

#统计状态数量
def count(number,cou_file):
    f=open(cou_file,'w')
    f.writelines(str(number).encode('UTF-8'))
    f.close

#状态内容
def publishstr(filename):
    publishlist=[]
    ffile=open(filename,'r')
    for line in ffile.readlines():
        publishlist.append(line)
    return publishlist




