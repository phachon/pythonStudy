# for 循环
# posts = ['产品部', '视频部', '测试部', '科技部']
# for post in posts:
# 	print(post)
# posts = ['产品部', '视频部', '测试部', '科技部', ['研发1', '研发2', '研发3']]
# for post in posts:
# 	print(post)
#
# numbers = [75, 92, 59, 68]
# total = 0
# for number in numbers:
# 	total += number
# s = total / 4
# print(s)
numbers1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number1 in numbers1:
	for number2 in numbers2:
		if number2 > number1:
			print(number2 * 10 + number1)
