"""
将客座率数据转换成矩阵形式
@author Panchao
"""

import xlrd
import xlwt
import os
import time
from railway.logger import Logger
from xlutils.copy import copy

runLog = Logger('logs/run.log')
errorLog = Logger('logs/error.log')


def read_data(file):
	""" 读取plf数据 """

	if os.path.isfile(file) is False:
		exit('file '+file+' not found')
	suffix = file.split('.')[-1]
	if suffix != ('xls' or 'xlsx'):
		exit('file type error, must .xls or .xlsx file')

	data = xlrd.open_workbook(file)
	sheet = data.sheet_by_name(u'data')
	# 总行数
	rowNumbers = sheet.nrows

	data = []
	train_numbers = []

	for i in range(rowNumbers):
		rowValue = sheet.row_values(i)

		if rowValue[0] == '车次':
			continue
		train_number = rowValue[0]
		runTime = rowValue[1]
		plf = rowValue[5]

		if train_number not in train_numbers:
			train_numbers.append(train_number)

	print(train_numbers)
		#print(runTime)
		#print(plf)
	exit()


if __name__ == '__main__':

	old_file = 'plf.xls'
	save_file = 'plf_matrix.xls'

	if not os.path.isfile(save_file):
		runLog.info('not found ' + save_file + ' file, is helping you create')
		write = xlwt.Workbook()
		write_sheet = write.add_sheet('data', cell_overwrite_ok=True)
		write.save(save_file)
		runLog.info('create file ' + save_file + ' success!')

	result = read_data(old_file)

