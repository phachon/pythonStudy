"""
dict key value 无序集合
"""

# 创建一个dict
info = {
	'name': 'pc',
	'age': 23,
	'sex': '男',
}
# info['ss'] = 89
# 添加一个元素
info.setdefault('title', '测试')

# 判断是否存在这个key
if 'name' in info:
	print(info['name'])
if 'age' in info:
	print(info['age'])
if 'post' in info:
	print(info['post'])
else:
	print("不存在post")
print(info)

# dict get 方法 不存在会返回none
print(info.get('name'))
print(info.get('age'))
post = info.get('post')
if post is None:
	print("不存在post")
else:
	print(post)
for key in info:
	print(key + "=>" + str(info[key]))
