"""
while 循环
"""

#while 循环
age = input("请输出你的你年龄")
age = int(age)
count = 1
while age < 18:
	print("Sorry,你还未成年!")
	if count == 3:
		print("你已经输入3次，退出")
		break
	age = input("请重新输出你的你年龄")
	age = int(age)
	count += 1
if age >= 18:
	print("你是成年人了")
print("结束！")
