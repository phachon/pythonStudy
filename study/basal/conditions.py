# python 条件语句
age = input("请输出你的18你年龄")
age = int(age)
if age <= 0:
	print("年龄输入错误")
elif 0 < age <= 10:
	print("哦，你是小学生")
elif 10 < age < 18:
	print("哦， 你是中学生")
elif 18 <= age < 22:
	print("哦，你是大学生了")
else:
	print("哦，你已经工作了")
print("结束")