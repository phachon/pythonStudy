"""
自定义函数
"""

import math


# 自定义求绝对值的函数
def get_absolute(number):
	if number <= 0:
		return -number
	else:
		return number


# 自定义square_of_sum 函数
def square_of_sum(l):
	p = [i * i for i in l]
	return sum(p)
print(square_of_sum([1, 2, 3, 4]))


# 返回多个值 x = (-b±√(b²-4ac)) / 2a
def quadratic_equation(a, b, c):
	t = math.sqrt(b * b - 4 * a * c)
	x1 = (-b + t) / (a * 2)
	x2 = (-b - t) / (a * 2)
	return x1, x2
a1, a2 = quadratic_equation(2, 8, 4)
print(a1, a2)


# 递归函数
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)
print(fact(10))


# 汉诺塔递归
def move(n, A, B, C):
	if n == 1:
		print(A + "移动到" + C)
		return
	move(n - 1, A, C, B)
	print(A + "移动到" + C)
	move(n - 1, B, A, C)

move(4, 'A', 'B', 'C')


# x 的 n 次方的函数
def power(x, n=2):
	i = 1
	b = 1
	while i <= n:
		b *= x
		i += 1
	return b
print(power(8))


# 可变参数传入
def test(*l):
	for n in l:
		print(n)
	return
test(1, 2, 3, 4)
