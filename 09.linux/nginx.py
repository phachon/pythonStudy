#!/usr/local/python3
"""
监控 linux 下 nginx 服务器进程
"""
import os, sys, time

while True:
	time.sleep(4)
	try:
		ret = os.popen('ps aux|grep nginx').readlines()
		if len(ret) < 2:
			print("nginx 进程异常，4秒后重启")
			time.sleep(3)
			os.system("sudo /usr/local/nginx -s reload")
	except Exception as e:
		print("error", e)
		exit()

