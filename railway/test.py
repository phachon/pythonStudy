'''
python 读取excel
'''
import xlrd
import xlwt
data = xlrd.open_workbook('20150101.xls')
sheet = data.sheet_by_name(u'Sheet1')

write = xlwt.Workbook()
write_sheet = write.add_sheet('data', cell_overwrite_ok=True)
write_sheet.write(0, 0, '车次')
write_sheet.write(0, 1, '时间')
write_sheet.write(0, 2, '下车时间')
write_sheet.write(0, 3, '上车时间')
write_sheet.write(0, 4, '上车人数')
write_sheet.write(0, 5, '下车人数')
write_sheet.write(0, 6, '站点')

nrows = sheet.nrows
ncols = sheet.ncols

# 始发日期
time = sheet.row_values(1)[0].split('：')[1].strip()
total = 0

def execute(data):

	number = len(data)
	trainInfo = data[0][0].split()
	# 车次
	train_number = trainInfo[0]
	# 车站范围
	train_range = trainInfo[1]
	# 日均定员
	person_average = trainInfo[6]
	# 客座率
	plf = trainInfo[-2]
	#上车总数集合
	up_total_list = data[-1]
	#下车时间集合
	down_time_list = data[2]

	new_data = []
	#print(down_time_list)
	for i in range(number):
		new_excel = []

		if '上车人数合计' in data[i][0]:
			continue
		if i > 2:
			down_time = data[i][1]
			up_time = down_time_list[i-1]
			up_total = up_total_list[i-1]
			down_total = data[i][number-3]
			station = data[i][0]

			new_excel.append(train_number)
			new_excel.append(time)
			new_excel.append(down_time)
			new_excel.append(up_time)
			new_excel.append(up_total)
			new_excel.append(down_total)
			new_excel.append(station)

			#print(new_excel)
			new_data.append(new_excel)
	return new_data


def get_data(nrows):
	data = []
	values = []
	for i in range(nrows):
		if i > 1:
			row_value = sheet.row_values(i)
			if '日均定员' in row_value[0]:
				data.clear()
				data.append(row_value)
				continue
			data.append(row_value)
			if '上车人数合计' in row_value[0]:
				for x in range(len(execute(data))):
					values.append(execute(data)[x])
				# exit()
	return values


for i in range(len(get_data(nrows))):
	row_data = get_data(nrows)[i]
	print(row_data)
	write_sheet.write(i + 1, 0, row_data[0])
	write_sheet.write(i + 1, 1, row_data[1])
	write_sheet.write(i + 1, 2, row_data[2])
	write_sheet.write(i + 1, 3, row_data[3])
	write_sheet.write(i + 1, 4, row_data[4])
	write_sheet.write(i + 1, 5, row_data[5])
	write_sheet.write(i + 1, 6, row_data[6])

write.save('data.xls')
