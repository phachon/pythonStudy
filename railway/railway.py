"""
python 读取excel
"""

import xlrd
import xlwt
import os


def each_file(filePath):
	""" 遍历指定目录下所有的文件 """

	allFiles = []
	listDir = os.listdir(filePath)
	for dir in listDir:
		if os.path.isfile(os.path.join(filePath, dir)):
			allFiles.append(os.path.join(filePath, dir))
		else:
			allFiles += each_file(os.path.join(filePath, dir))
	return allFiles


def analysis_file_data(file):
	""" 按车次整合数据 """

	if os.path.isfile(file) is False:
		exit('file '+file+' not found')
	suffix = file.split('.')[-1]
	if suffix != ('xls' or 'xlsx'):
		exit('file type error, must .xls or .xlsx file')
	fileName = os.path.split(file)[1]

	runTime = fileName.split('.')[0]
	data = xlrd.open_workbook(file)
	sheet = data.sheet_by_name(u'Sheet1')
	# 总行数
	rowNumbers = sheet.nrows
	# 总列数
	colNumbers = sheet.ncols

	values = []
	data = []

	for i in range(rowNumbers):
		if i > 1:
			rowValue = sheet.row_values(i)
			# print(rowValue[0])
			if '数据源 客票席位汇总数据' in rowValue[0]:
				break
			data.append(rowValue)
			if '上车人数合计' in rowValue[0]:
				values.append(data)
				data = []

	return runTime, values


def recomb_data(runTime, values):
	""" 解析数据重新组合 """

	for i in range(len(values)):

		trainValues = values[i]
		trainInfo = trainValues[0][0].split()
		# 车次
		trainNumber = trainInfo[0]
		# 车站范围
		train_range = trainInfo[1]
		# 日均定员
		person_average = trainInfo[6]
		# 客座率
		plf = trainInfo[-2]
		# 上车人数集合
		onPersonList = trainValues[-1]
		# 下车时间集合
		offTimeList = trainValues[2]

		for y in range(len(trainValues)):
			if y > 0:
				print(trainValues[y])
				exit()

if __name__ == '__main__':
	time, values = analysis_file_data('20150101.xls')
	recomb_data(time, values)
