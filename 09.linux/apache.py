#!/usr/local/python3
"""
监控 linux 下 apache 服务器进程
"""
import os, time

while True:
	time.sleep(4)
	try:
		ret = os.popen('ps aux|grep apche').readlines()
		if len(ret) > 2:
			print("apache 进程开启，3秒后关闭")
			time.sleep(3)
			os.system("sudo service httpd stop")
			exit()
	except Exception as e:
		print("error", e)
		exit()

