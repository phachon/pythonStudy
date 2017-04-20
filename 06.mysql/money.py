import mysql.connector
import sys


class TransferMoney(object):
	def __init__(self, conn):
		self.conn = conn

	def execute(self, transferId, receiveId, money):

		try:
			#转账id和接收id是否存在
			self.checkAccount(transferId)
			self.checkAccount(receiveId)
			#转账账户钱是否够
			self.checkMoney(transferId, money)
			#转账账户减钱
			self.reduceMoney(transferId, money)
			#接收账户加钱
			self.addMoney(receiveId, money)

			self.conn.commit()
		except Exception as e:
			self.conn.rollback()
			raise e

	# 检查账户是否合法
	def checkAccount(self, accountId):
		cursor = self.conn.cursor()

		try:
			sql = 'select * from money where account_id=%s' % accountId
			cursor.execute(sql)

			result = cursor.fetchall()
			if len(result) != 1:
				raise Exception("该用户不存在")
		except Exception as e:
			raise e
		finally:
			cursor.close()

	# 检查账户钱是否足够
	def checkMoney(self, accountId, money):

		cursor = self.conn.cursor()

		try:
			sql = 'select * from money where account_id=%s and money>%s' % (accountId, money)
			cursor.execute(sql)
			result = cursor.fetchall()

			if len(result) != 1:
				raise Exception("转账账户资金不足"+money)
		finally:
			cursor.close()

	# 减钱
	def reduceMoney(self, accountId, money):

		cursor = self.conn.cursor()

		try:
			sql = 'update money set money=money-%s where account_id=%s' % (money, accountId)
			cursor.execute(sql)
			result = cursor.rowcount
			if result != 1:
				raise Exception('转账出账失败')
		finally:
			cursor.close()

	# 增加钱
	def addMoney(self, accountId, money):

		cursor = self.conn.cursor()

		try:
			sql = 'update money set money=money-%s where account_id=%s' % (money, accountId)
			cursor.execute(sql)
			result = cursor.rowcount
			if result != 1:
				raise Exception('转账进账失败')
		finally:
			cursor.close()


if __name__ == '__main__':
	transferId = sys.argv[1]
	receiveId = sys.argv[2]
	money = sys.argv[3]

	# 数据库连接
	conn = mysql.connector.connect(user='root', password='123456', database='bms_account')

	transferMoney = TransferMoney(conn)
	try:
		transferMoney.execute(transferId, receiveId, money)
	except Exception as e:
		print("转账出错：" + str(e))
	finally:
		conn.close()