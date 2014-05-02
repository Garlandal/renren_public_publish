#!/usr/bin/python
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
import urllib2
import urllib
import time
import re


#抓取前端周刊的文章并写入文件
def qianduans():
    f=open(r'qianduanio.txt','w')
    for page in range(1, 1000):
        urls = 'http://www.feweekly.com/issues/' + str(page)
        print urls
        try:
            d = pq(urls)
            content0 = []
            for i in range(0, 50):
                m = d('h2').eq(i).html()
                if m:
                    if len(m) == 4:
                        x = m
                    if len(m) > 20:
                        a = pq(m)
                        content = '[' + x + ']' + ':' + d('h2').eq(i).text() + a('a').attr('href')
                        f.writelines(content.encode('Utf-8')+'\n')
        except urllib2.HTTPError, e:
            f.close()
            break
    return 'qianduanio.txt'

if __name__ =="__main__":
    qianduans()
