# DB 操作类


class DB:
	def __init__(self, host, port, user, password, database, charset):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.database = database
		self.charset = charset


	def select_all(self, sql):
		self.sql = sql
