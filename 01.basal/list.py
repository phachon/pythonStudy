"""
list 数据类型
"""

# list 数据类型
# 创建list
students = ['pha', 'tony', 'black', 'red']
# 创建包含不同数据类型的list
post = ['产品部', '测试部', '技术部']
# 创建空的list
empty = []

# demo
className = ['Admin', 95.5, 'Lisa', 85, 'Bart', 59]
# print("学生list:\n")

print("按照索引取第一个部门是:" + post[0])
print("按照索引取最后一个部门是:" + post[-1])

# 添加 append 添加到尾部
post.append("视频部")
print(post)
# 添加 insert
post.insert(2, "销售部")
post.insert(3, "科技部")
print(post)

# 删除 pop 删除尾部
post.pop()
print(post)
# 删除一个索引位置的部门
post.pop(3)
print(post)

# 替换
post[0] = '技术产品部'
print(post)

# key 是否存在
if 'a' in classmethod:
	print('存在')
