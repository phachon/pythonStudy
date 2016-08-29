#!/usr/local/python3
"""
返回 linux 负载信息
"""


def load():
	loadavg = {}
	f = open("/proc/loadavg")
	con = f.read().split()
	f.close()
	loadavg['lavg_1'] = con[0]
	loadavg['lavg_5'] = con[1]
	loadavg['lavg_15'] = con[2]
	loadavg['nr'] = con[3]
	loadavg['last_pid'] = con[4]
	return loadavg

print("loadavg", load()['lavg_15'])
