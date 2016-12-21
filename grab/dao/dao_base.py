"""
dao 基类
@author panchao
@time 2016-08-31
"""
from grab.core.DB import DB


class DaoBase(object):

	def __init__(self):
		self.DB = DB()
