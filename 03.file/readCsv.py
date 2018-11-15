import csv

file = open('data/JData_Action_201604.csv', encoding='utf-8')
csv_reader = csv.reader(file)

for row in csv_reader:
	print(row)
	exit()