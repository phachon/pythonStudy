'''
对MySQLdb常用函数进行封装的类
 整理者：兔大侠和他的朋友们（http://www.tudaxia.com）
 日期：2014-04-22
 出处：源自互联网，共享于互联网:-)

 注意：使用这个类的前提是正确安装 MySQL-Python模块。
 官方网站：http://mysql-python.sourceforge.net/
'''

import mysql.connector
import time


class MySQL:
	u'''对MySQLdb常用函数进行封装的类'''

	error_code = ''  # MySQL错误号码

	_instance = None  # 本类的实例
	_conn = None  # 数据库conn
	_cur = None  # 游标

	_TIMEOUT = 30  # 默认超时30秒
	_timecount = 0

	def __init__(self, dbconfig):
		u'构造器：根据数据库连接参数，创建MySQL连接'
		try:
			self._conn = mysql.connector.connect(host=dbconfig['host'],
			                             port=dbconfig['port'],
			                             user=dbconfig['user'],
			                             password=dbconfig['passwd'],
			                             database=dbconfig['db'],
			                             charset=dbconfig['charset'])
		except mysql.connector.Error as e:
			self.error_code = e.args[0]
			error_msg = 'MySQL error! ', e.args[0], e.args[1]
			print(error_msg)

			# 如果没有超过预设超时时间，则再次尝试连接，
			if self._timecount < self._TIMEOUT:
				interval = 5
				self._timecount += interval
				time.sleep(interval)
				return self.__init__(dbconfig)
			else:
				raise Exception(error_msg)

		self._cur = self._conn.cursor()
		self._instance = mysql.connector

	def query(self, sql):
		u'执行 SELECT 语句'
		try:
			self._cur.execute("SET NAMES utf8")
			result = self._cur.execute(sql)
		except mysql.connector.Error as e:
			self.error_code = e.args[0]
			print("数据库错误代码:", e.args[0], e.args[1])
			result = False
		return result

	def fetchRows(self):
		return self._cur.fetchall()

	def fetchOne(self):
		return self._cur.fetchone()

	def getRowCount(self):
		return self._cur.rowcount

	def commit(self):
		self._conn.commit()

	def rollback(self):
		self._conn.rollback()

	def __del__(self):
		u'释放资源（系统GC自动调用）'
		try:
			self._cur.close()
			self._conn.close()
		except:
			pass

	def close(self):
		self.__del__()