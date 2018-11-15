import pandas as pandas

data = pandas.read_csv('data/JData_Action_201604.csv')

# 返回前n条数据, 默认返回5条
rows = data.head(10)
print(rows)
# 返回全部列名
cols = data.columns
print(cols)