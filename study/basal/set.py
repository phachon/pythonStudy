# set 无序集合，没有重复
#创建 set
l = ['video', 'live', 'topic']
s = set(l)
#包含重复元素的时候。会自动过滤掉
p = set(['A', 'B', 'C', 'C'])

print(s)
print(p)
print(len(p))

if 'A' in p:
	print("p 里包含A")
else:
	print("p 里不包含A")
#------------------------------------------------------------------------------------
# set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快。
#
# set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
#
# 最后，set存储的元素也是没有顺序的。
#------------------------------------------------------------------------------------
#添加set
p.add('D')
print(p)
#删除set
p.remove('B')
print(p)