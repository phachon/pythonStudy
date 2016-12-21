"""
url dao 层
@author panchao
@time 2016-08-31
"""
from grab.dao.dao_base import DaoBase


class DaoUrl(DaoBase):

	__table__ = 'grab_url'
	__db__ = 'video_grab'
	__primary_key__ = 'url_id'

	status_default = '0'
	status_failed = '-1'
	status_success = '1'

	# 获取所有的url
	def getUrls(self):
		return self.DB\
			.select('*')\
			.froms(self.__table__)\
			.execute(self.__db__)\
			.fetchAll()

	# 根据状态获取url
	def getUrlsByStatus(self, status):
		return self.DB\
			.select('*')\
			.froms(self.__table__)\
			.where('status', '=', status)\
			.execute(self.__db__)\
			.fetchAll()

	# 根据主键修改url
	def updateUrlsByUrlId(self, values, urlId):
		if not urlId:
			return False
		return self.DB\
			.update(self.__table__)\
			.set(values)\
			.where(self.__primary_key__, '=', urlId)\
			.execute(self.__db__)\
			.rowCount()