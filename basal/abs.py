x = input('请输入一个值')
x = int(x)
def my_abs(y):
	if y >= 0:
		return y
	else:
		return -y

print(my_abs(x))