"""
url 业务逻辑层
@author panchao
@time 2016-08-31
"""
from grab.bass.bass_base import BassBase
from grab.dao.dao_url import DaoUrl


class BassUrl(BassBase):

	# 获取所有的 url
	def getUrls(self):
		return DaoUrl().getUrls()

	# 获取默认的 url
	def getDefaultUrls(self):
		return DaoUrl().getUrlsByStatus(DaoUrl.status_default)