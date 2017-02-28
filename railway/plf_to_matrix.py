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


def read_data(file, save_file):
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

	train_numbers = []
	runTimes = []

	for i in range(rowNumbers):
		print("第 "+i+" 行开始")
		rowValue = sheet.row_values(i)
		if len(rowValue) is 0:
			continue
		if rowValue[0] == '车次':
			continue
		train_number = rowValue[0]
		runTime = rowValue[1]
		plf = rowValue[5]

		if train_number not in train_numbers:
			train_numbers.append(train_number)

		if runTime not in runTimes:
			runTimes.append(runTime)

		row = train_numbers.index(train_number) + 1
		line = runTimes.index(runTime) + 1

		write_file(line, row, plf, save_file)

	for x in range(len(runTimes)):
		write_file(x+1, 0, runTimes[x], save_file)
	for y in range(len(train_numbers)):
		write_file(0, y+1, train_numbers[y], save_file)

	print(len(train_numbers))


def write_file(line, row, value, file='plf_matrix.xls'):
	""" 安坐标写入 """

	old_data = xlrd.open_workbook(file)
	write = copy(old_data)
	write_sheet = write.get_sheet(0)
	write_sheet.write(line, row, value)
	write.save(file)

if __name__ == '__main__':

	old_file = 'plf.xls'
	save_file = 'plf_matrix.xls'

	if not os.path.isfile(save_file):
		runLog.info('not found ' + save_file + ' file, is helping you create')
		write = xlwt.Workbook()
		write_sheet = write.add_sheet('data', cell_overwrite_ok=True)
		write.save(save_file)
		runLog.info('create file ' + save_file + ' success!')

	read_data(old_file, save_file)

