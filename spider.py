#!/usr/bin/python
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq

import urllib2
import urllib
import time
import re

#judge time
def timecheck(begin=0730,end=2350):
    xtime = int(time.strftime("%H%M", time.localtime()))
    if xtime >= begin and xtime < end:
        return 1
    else:
        time.sleep(60)
        return timecheck()

#count issue number
def count(number,cou_file):
    f=open(cou_file,'w')
    f.writelines(str(number).encode('UTF-8'))
    f.close

#load content
def publishstr(filename):
    ffile=open(filename,'r')
    publishlist = [line for line in ffile.readlines()]
    return publishlist

# get title and link from manongio and write to file
def manongs():
    with open('manongio.txt', 'w') as f:
        for page in range(1, 1000):
            content = urllib.urlopen(
                'http://weekly.manong.io/issues/' + str(page)).read()
            if len(content) > 1000:
                type_list = ['>程序设计', '>编程语言', '>工具资料', '>编程之外', '>每周一书', '>赞助我们']
                for i in range(0, 5):
                    html_code = content[content.find(type_list[i]):content.find('<h3>', content.find(type_list[i]))]
                    pat0 = re.compile(r'<a target="_blank" href.+?</a>')
                    html_block = re.findall(pat0, html_code)
                    for title_url in html_block:
                        p = pq(title_url)
                        x = p('a').text() + ':' + p('a').attr('href')
                        con = '[' + html_code[1:13] + ']' + x.encode("UTF-8")
                        f.writelines(str(con)+'\n')
            else:
                break


#get title and link from feweekly and write to file
def qianduans():
    with open(r'qianduanio.txt', 'w') as f:
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
                break

if __name__ =="__main__":
    manongs()
    qianduans()
