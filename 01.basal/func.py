"""
python 函数
"""

# python 函数
L = [x * x for x in range(1, 101)]
print(sum(L))

l = range(1, 101)
s = []
for p in l:
	s.append(p * p)
print(sum(s))

i = 1
m = []
while i < 101:
	m.append(i * i)
	i += 1
sum(m)
print(sum(m))
