#!/usr/bin/python
# -*- coding:utf-8 -*-

from logpubish import spider
from manongs import manongs
from qianduans import qianduans
from timesave import timecheck, count, publishstr
import time

if __name__ == "__main__":
    renrenspider = spider('主頁管理員帳號', '主頁管理員密碼')
    try:
        renrenspider.login()
    except ValueError, e:
        localtime = time.strftime(
            '%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        print 'login error' + localtime
        time.sleep(43200)
    finally:
        renrenspider.login()
        while True:
        	if time.strftime("%a%H",time.localtime()) == 'Sat07':
            	    manongs()
            	    qianduans()
        	if timecheck():
        		numberx = open(r'ma_co.txt', 'r').readlines()
                numbery = open(r'qian_co.txt', 'r').readlines()
                number1 = int(str(numberx[0]))
                number2 = int(str(numberx[0]))
                pubcon1 = publishstr('manongio.txt')[number1]
                pubcon2 = publishstr('qianduanio.txt')[number2]
                renrenspider.publish(pubcon1)
                count(number1 + 1, 'ma_co.txt')
                time.sleep(7200)
                renrenspider.publish(pubcon2)
                count(number2 + 1, 'qian_co.txt')
                time.sleep(7200)
            


            
            


