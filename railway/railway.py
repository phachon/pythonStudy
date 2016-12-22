"""
python 读取excel
"""

import xlrd
import xlwt
import os
from xlutils.copy import copy


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

	results = []
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

		# 上车站对应时间与上车站对应人数字典
		upStationTime = {}
		upStationPerson = {}
		for y in range(len(trainValues[1])):
			if 'ZD' in trainValues[1][y]:
				upStationTime[trainValues[1][y]] = offTimeList[y]
				upStationPerson[trainValues[1][y]] = onPersonList[y]

		for z in range(len(trainValues)):
			if '上车人数合计' in trainValues[z][0]:
				results.append([trainNumber, time, trainValues[z-1][1], '', '', trainValues[z-1][2 + len(upStationTime)], trainValues[z-1][0]])
				break
			if z > 2:
				#print(trainValues[z])
				# 站点
				stationNumber = trainValues[z][0]

				if stationNumber not in upStationTime.keys():
					# TODO 记录日志，标出该数据有问题
					continue
				# 上车时间
				upTime = upStationTime[stationNumber]
				# 下车时间
				if (z is 3) and (trainValues[z][1] is ''):
					offTime = upTime
				else:
					offTime = trainValues[z][1]
				# 上车人数
				upPerson = upStationPerson[stationNumber]
				# 下车人数
				offPerson = trainValues[z][2 + len(upStationTime)]

				results.append([trainNumber, time, offTime, upTime, upPerson, offPerson, stationNumber])
	return results


def write_file(values, file='data.xls', startRow=0):
	""" 写入整合好的数据到文件 """

	old_data = xlrd.open_workbook(file)
	write = copy(old_data)
	write_sheet = write.get_sheet(0)

	for i in range(len(values)):
		write_sheet.write(startRow + i + 1, 0, values[i][0])
		write_sheet.write(startRow + i + 1, 1, values[i][1])
		write_sheet.write(startRow + i + 1, 2, values[i][2])
		write_sheet.write(startRow + i + 1, 3, values[i][3])
		write_sheet.write(startRow + i + 1, 4, values[i][4])
		write_sheet.write(startRow + i + 1, 5, values[i][5])
		write_sheet.write(startRow + i + 1, 6, values[i][6])
	write.save(file)


if __name__ == '__main__':

	data_dir = '2015/01'
	save_file = 'data.xls'
	rowCounts = 0

	if not os.path.isfile(save_file):
		exit('sorry not found '+save_file+' file, please create')

	files = each_file(data_dir)
	for i in range(len(files)):
		print(files[i])
		time, values = analysis_file_data(files[i])
		results = recomb_data(time, values)
		if i > 0:
			rowCounts = len(results)
		write_file(results, save_file, rowCounts)

