#!/usr/bin/python
# -*- coding:utf-8 -*-

from pyquery import PyQuery as pq
import urllib2
import urllib
import time
import re


# 抓取码农周刊的文章并写入文件
def manongs():
    f=open(r'manongio.txt','w')
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
            f.close()
            break
    return 'manongio.txt'

if __name__ =="__main__":
    manongs()