#!/usr/local/python3
"""
返回 linux 内存使用
"""
from collections import OrderedDict


def memory():
	memoryInfo = OrderedDict()
	with open('/proc/meminfo') as f:
		for line in f:
			memoryInfo[line.split(':')[0]] = line.split(':')[1].strip()
	return memoryInfo

if __name__ == "__main__":
	memory = memory()
	print("总共内存：%s" % memory['MemTotal'])
	print("剩余内存：%s" % memory['MemFree'])
