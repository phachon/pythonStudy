#!/usr/local/python
#-*- coding: utf-8 -*-
"""
sphinx 重建索引并重启
usage: > python sphinx.py show development
"""
import os
import sys

__author__ = "panchao"
__date__ = "$2017-03-07$"


class RebuildSphinx(object):
	""" 删除索引重建并重启 """

	# root dir
	_rootPath = ''
	# env mapping
	_envMapping = ['development', 'staging', 'production']
	# run env
	_env = ''
	# sphinx task name
	_taskName = ''
	# sphinx etc conf
	_etcFile = ''
	# sphinx install dir
	_sphinxPath = '/usr/local/sphinx/'

	def __init__(self, taskName, env):
		""" init """

		self._rootPath = os.path.split(os.path.realpath(__file__))[0]
		self._taskName = taskName
		self._env = env

	def checkDir(self):
		""" 检查目录和配置的合法 """

		if self._env not in self._envMapping:
			raise Exception('Execute env params error!')

		self._etcFile = os.path.realpath(self._rootPath + '/../etc/' + env + '/' + self._taskName + '.conf')
		if not os.path.isfile(self._etcFile):
			raise Exception('Execute etc conf not found!')

		return True

	def deleteIndexerData(self):
		""" 删除索引文件 """

		indexerDataPath = os.path.realpath(self._sphinxPath + 'var/data/' + self._taskName)

		if os.path.isdir(indexerDataPath) is False:
			os.mkdir(indexerDataPath, 777)

		try:
			os.popen('rm -rf ' + indexerDataPath + '/*')
		except Exception as e:
			raise Exception('Delete index data error: ' + e)

		print('Delete indexer data finished!')

		return True

	def killSearched(self):
		""" 杀死sphinx进程 """

		searchdPath = self._sphinxPath + 'bin/searchd'

		try:
			readInfo = os.popen('ps aux|grep ' + self._taskName + '.conf').readlines()
		except Exception as e:
			raise ('Find sphinx searchd thread error: ' + e)

		for text in readInfo:
			colum = text.split()
			pid = colum[1]
			searchd = colum[10]
			if searchd != searchdPath:
				continue
			try:
				os.popen('kill ' + str(pid))
			except Exception as e:
				raise Exception('Kill searched pid ' + str(pid) + ' error: ' + e)
			print('Kill searchd pid ' + str(pid) + ' finished!')

		return True

	def reBuild(self):
		""" 重建索引并重启searchd """

		indexer = self._sphinxPath + 'bin/indexer'
		searchd = self._sphinxPath + 'bin/searchd'

		indexerCmd = indexer + ' --config ' + self._etcFile + ' --all --rotate'
		searchdCmd = searchd + ' --config ' + self._etcFile

		try:
			os.popen(indexerCmd)
		except Exception as e:
			raise Exception('Rebuild sphinx indexer failed: ' + e)
		print('Rebuild sphinx indexer finished!')

		try:
			os.popen(searchdCmd)
		except Exception as e:
			raise Exception('Restart sphinx searched failed: ' + e)
		print('Restart sphinx searched finished!')

		return True

	def execute(self,):
		""" 执行 """

		print('Rebuild indexer and searchd start')

		try:
			self.checkDir()
			self.deleteIndexerData()
			self.killSearched()
			self.reBuild()
		except Exception as e:
			print(e)

		print('Rebuild indexer and restart searchd end')

def error(errorInfo, isHelp=False):
	message = ''
	if errorInfo is not '':
		message += "Error: " + errorInfo + "\r\n\n"
	if isHelp is True:
		message += "Usage: python sphinx.py [SphinxTask] [Env]\r\n"
		message += "SphinxTask:\r\n" \
		           "    Sphinx task name, must exist in the etc dir [task].conf \r\n" \
		           "Env:\r\n" \
		           "   development   development environment\r\n" \
		           "   production    production environment\r\n" \
		           "   staging       staging environment\r\n" \
		           "Example:\r\n" \
		           "   python sphinx.py show development\r\n" \
		           "   python sphinx.py show_stream production\r\n"

	exit(message)

if __name__ == '__main__':

	optionNumber = len(sys.argv)
	if optionNumber < 3:
		error('execute option error!', True)
	taskName = sys.argv[1]
	env = sys.argv[2]
	if taskName == '':
		error('execute params taskName error', True)

	try:
		sphinxTask = RebuildSphinx(taskName, env)
		sphinxTask.execute()
	except Exception as e:
		error(e)