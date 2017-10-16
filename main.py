#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time

def strMul(strNum):
	i = int(strNum)
	i = i-1
	s = str(i)
	while(len(s)<6):
		s='0'+s
	return s

num = "578999"
url="http://www.xiaoshuowu.com/book/"

while(int(num)>0):
	try:
		mURL = url+num+"/"
		r = requests.get(mURL)
		r.encoding=r.apparent_encoding
		soup = BeautifulSoup(r.text,'html.parser')
		try:
			mTitle = soup.body.select('span')[0].get_text()
			mAuthor = soup.body.select('a')[31].get_text()
			mClass = soup.body.table.tr.td.get_text().split("：")[1]
			print(mURL+" 标题："+mTitle+" 作者："+mAuthor+" 类型："+mClass)
		except:
			print("未找到指定文本，尝试重试")
			try:
				time.sleep(2)
				r = requests.get(mURL)
				r.encoding=r.apparent_encoding
				soup = BeautifulSoup(r.text,'html.parser').body
				mTitle = soup.select('span')[0].get_text()
				mAuthor = soup.select('a')[31].get_text()
				mClass = soup.table.tr.td.get_text().split("：")[1]
				print(mURL+" 标题："+mTitle+" 作者："+mAuthor+" 类型："+mClass)
			except:
				print("重新查找失败，跳过该网页")
		num = strMul(num)
		#time.sleep(1)
	except:
		print("未找到")
	
	
	
