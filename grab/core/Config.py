"""
配置文件加载类
@author panchao
@time 2016-08-31
"""
import grab.config.development as development
import grab.config.development as production
import grab.config.development as testing


class Config(object):

	_environment = 'development'
	_config = {}
	_data = []

	def __init__(self):
		if self._environment == 'development':
			self._config = development.configs
		elif self._environment == 'production':
			self._config = production.configs
		elif self._environment == 'testing':
			self._config = testing.configs
		else:
			self._config = development.configs

	def load(self, param):
		data = param.split('.')
		if len(data) == 0:
			return None
		if len(data) == 1:
			return self._config[data[0]]
		if len(data) == 2:
			return self._config[data[0]][data[1]]
		if len(data) > 2:
			print('param error')
			exit()
