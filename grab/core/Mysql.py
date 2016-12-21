#!/usr/local/python3
"""
Mysql 操作类
"""
import mysql.connector


class Mysql(object):

	_host = '127.0.0.1'
	_port = '3306'
	_user = 'root'
	_password = '123456'
	_database = ''
	_charset = 'utf8'
	_conn = None
	_cursor = None

	def __init__(self, config):
		self._host = config['host']
		self._port = config['port']
		self._user = config['user']
		self._password = config['password']
		self._database = config['database']
		self._charset = config['charset']

	def connect(self):
		try:
			self._conn = mysql.connector.connect(host=self._host, port=self._port, user=self._user, password=self._password,
		                                     database=self._database, charset=self._charset)
		except mysql.connector.Error as e:
			print('数据库连接出错: %s' % e)
			exit()

	def query(self, sql):
		self._cursor = self._conn.cursor(dictionary=True)

		try:
			self._cursor.execute(sql)
		except mysql.connector.Error as e:
			print('数据库执行出错: %s' % e)
			self._cursor.close()
			self._conn.close()

	def fetchAll(self):
		return self._cursor.fetchall()

	def fetchOne(self):
		return self._cursor.fetchOne()

	def rowCount(self):
		return self._cursor.rowcount

	def result(self):
		return self._cursor

	def __del__(self):
		try:
			self._cursor.close()
			self._conn.close()
		except:
			pass

