#range
#l = [i * (i + 1) for i in range(1, 101, 2)]
#print(l)


def pp(l):
	return [i.upper() for i in l if isinstance(i, str) is True]
print(pp(['ada', 'lkjkl', 'ytuty', 'eyu', 89798]))