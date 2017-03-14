from functools import reduce


def factorial(x, y):
	return x * y


def ll(n):
	return list(range(1, n+1))


n = 5
result = reduce(factorial, ll(n))
print(result)
