#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import json
import re
import time 
import datetime


class spider():

	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.domain = 'renren.com'

		self.session = requests.session()
		self.token = {}

	def login(self):
		print '開始登錄'
		url = 'http://www.renren.com/PLogin.do'
		postdata = {
				'email': self.email,
				'password': self.password,
				'domain': self.domain
				}
		headers = {
				'Use-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
				}
		resp = self.session.post(url, data=postdata, headers=headers)
		pat0 = re.compile("get_check:'(.*)',get_check_x:'(.*)',env",re.DOTALL)
		pat1 = re.compile("'ruid':'(.*)',")
		results1 = pat0.search(resp.text)
		results2 = pat1.search(resp.text)
		self.tok = results1.group(1)
		self.rtk = results1.group(2)
		self.ids = results2.group(1)


	def publish(self, content):
#		url1 = 'http://shell.renren.com/人人ID/status'
		url = 'http://page.renren.com/jomo/act/status/saveStatus?pid=人人ID'
		headers = {
				'Use-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
				'Referer': 'http://shell.renren.com/ajaxproxy.htm'
				}
		post_data = {
				'content': content,
				'hostid': self.ids,
				'requestToken': self.tok,
				'_rtk': self.rtk,
				'channel': 'renren'
				}
		resp = self.session.post(url, data=post_data, headers=headers)
		# print resp.text
		print '%s:刚才使用你的人人账号 %s 发了一条状态内容为：(%s)' % (datetime.datetime.now(), self.email, post_data.get('content', '')) 



if __name__ == '__main__':
	renrenspider = spider('人人帳號', '密碼')
	renrenspider.login()
	content = raw_input('please input:')
	renrenspider.publish(content)
