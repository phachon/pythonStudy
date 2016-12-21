"""
连接 Mysql 操作类
@author panchao
@time 2016-08-31
"""
from grab.core.Config import Config
from grab.core.Mysql import Mysql


class DB(object):

	_sql = ''
	_instance = None
	_mysqlObject = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(DB, cls).__new__(cls, *args, **kwargs)
		return cls._instance

	def select(self, param):
		self._sql = 'select %s' % param
		return self._instance

	def insert(self, table):
		self._sql = 'insert into %s' % table
		return self._instance

	def update(self, table):
		self._sql = 'update %s' % table
		return self._instance

	def delete(self, table):
		self._sql = 'delete from %s' % table
		return self._instance

	def froms(self, table):
		self._sql += ''.join([' from ', table])
		return self._instance

	def where(self, column, sign, value):
		self._sql += ''.join([' where ', column, sign, "'", value, "'"])
		return self._instance

	def and_where(self, column, sign, value):
		self._sql += ''.join([' and ', column, sign, "'", value, "'"])
		return self._instance

	def or_where(self, column, sign, value):
		self._sql = ''.join([' or ', column, sign, "'", value, "'"])
		return self._instance

	def set(self, columns):
		data = []
		for key in columns:
			data.append(key+'='+"'"+columns[key]+"'")
		self._sql = self._sql + ' set ' + ','.join(data)
		return self._instance

	def columns(self, columns):
		self._sql = self._sql + " (" + ','.join(columns) + ")"
		return self._instance

	def values(self, values):
		self._sql = self._sql + " values ('" + "','".join(values) + "')"
		return self._instance

	def number(self, number):
		# self._sql = self._sql + ' limit ' + number + ','
		self._sql += ''.join([' limit ', number, ','])
		return self._instance

	def offset(self, offset):
		self._sql += offset
		return self._instance

	def order_by(self, column, type):
		self._sql += ''.join([' ORDER BY ', "'", column, "'", type])
		return self._instance

	def execute(self, db):

		config = Config().load('database.' + db)
		mysql = Mysql(config)
		mysql.connect()
		mysql.query(self._sql)

		return mysql

	def debug(self):
		print(self._sql)
		exit()
# DB = DB()
#
# r = DB.select('*').froms('grab_account').execute('video_grab').fetchAll()
#
# print(r)