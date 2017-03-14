#python slice切片
# 取前3个元素
names = ['aa', 'dd', 'cc', 'ee', 'mm']
i = 1
l = []
for i in range(3):
	l.append(names[i])
	i += 1
print(l)


#提供更简便的方法来获取 从索引0开始取，直到索引3为止，但不包括索引3
# print(names[0:3])
# print(names[:3])
# print(names[1:3])
# #表示从头切到尾
# print(names[:])
# #第三个参数每3个取一个
# print(names[::3])

#字符串进行切片
tt = 'ladnlkasndoisncoscasilasdn'
tt = tt.upper()
print(tt)
print(tt[1:3])


def first_upper(string):
	return string[0:1].upper() + string[1:]
print(first_upper('test'))

for i in range(1, 101):
	if i % 7 == 0:
		print(i)

for index, name in enumerate(names):
	print(index, "-->", name)

d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
for key, value in d.items():
	print(key, '==>', value)
