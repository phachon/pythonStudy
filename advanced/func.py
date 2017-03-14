from functools import reduce
#高阶函数
import time


def add(x, y, f):
	return f(x) + f(y)
# print(add(-5, -6, abs))


#map() 内置函数：传入一个参数，返回需要用 list()
def f(x):
	return x * x
l = [1, 2, 3, 4, 5, 6]
# print(list(map(f, l)))


#reduce() 内置函数：传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f
def m(x, y):
	return int(x) + int(y)
# print(reduce(m, l))


#filter() 内置函数：根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。返回需要用 list()
def delete_odd(x):
	if x % 2 == 0:
		return False
	else:
		return True
# print(list(filter(delete_odd, l)))


def is_not_empty(s):
	return s and len(s.strip()) > 0
n = ['test', None, '', 'str', '  ', 'END']
# print(list(filter(is_not_empty, n)))


#函数返回函数
def return_def():
	print("返回函数g...")
	def g():
		print("我是函数g")
	return g()


#闭包函数
def f_ll(number):
	print("闭包函数")
	def p():
		print(number)
	return p()

#装饰器
def f1(x):
	return x * 2

def new_f(f):
	def fn(x):
		print('call' + f.__name__ + '()')
		return f(x)
	return fn
g1 = new_f(f1)
print(g1(5))
f1 = new_f(f1)
print(f1(5))

def performance(f):
	def fn(*args, **kw):
		start_time = time.time()
		r = f(*args, **kw)
		end_time = time.time()
		print('run %s() time %fs:' % (f.__name__, (end_time - start_time)))
		return r
	return fn

@performance
def factorial(n):
	return reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial(10))
