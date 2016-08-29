#!/usr/local/python3
from collections import OrderedDict


def cpu_info():
	''' Return the information in /proc/cpuinfo
as a dictionary in the following format:
cpu_info['proc0']={...}
cpu_info['proc1']={...}
'''
	cpuInfo = OrderedDict()
	processor_info = OrderedDict()

	processor_number = 0
	with open('/proc/cpuinfo') as f:
		for line in f:
			if not line.strip():
				cpuInfo['processor%s' % processor_number] = processor_info
				processor_number += 1
				processor_info = OrderedDict()
			else:
				if len(line.split(':')) == 2:
					processor_info[line.split(':')[0].strip()] = line.split(':')[1].strip()
				else:
					processor_info[line.split(':')[0].strip()] = ''

	return cpuInfo

if __name__ == '__main__':
	cpu_info = cpu_info()
	for processor in cpu_info.keys():
		print(cpu_info[processor]['model name'])
