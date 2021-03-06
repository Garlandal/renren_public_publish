#!/usr/bin/python
# -*- coding:utf-8 -*-

from logpubish import Spider
from spider import timecheck, count, publishstr, qianduans, manongs

import time

if __name__ == "__main__":
    renrenspider = Spider('人人帳號', '密碼')
    while True:
		if timecheck():
			try:
				renrenspider.login()
			except ValueError, e:
				localtime = time.strftime(
						'%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
				print 'login error' + localtime
				time.sleep(43200)
				renrenspider.login()
			finally:
				if time.strftime("%a%H",time.localtime()) == 'Sat07':
					manongs()
					qianduans()
				numberx = open(r'ma_co.txt', 'r').readlines()
                numbery = open(r'qian_co.txt', 'r').readlines()
                number1 = int(str(numberx[0]))
                number2 = int(str(numberx[0]))
                pubcon1 = publishstr('manongio.txt')[number1]
                pubcon2 = publishstr('qianduanio.txt')[number2]
                renrenspider.publish(pubcon1)
                count(number1 + 1, 'ma_co.txt')
                time.sleep(14400)
                renrenspider.publish(pubcon2)
                count(number2 + 1, 'qian_co.txt')
                time.sleep(14400)
