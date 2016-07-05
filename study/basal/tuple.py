#python 元组
#元组的创建,一旦创建不可改变
# post = ('产品部', '视频部', '科技部')
# #创建空的元组
# empty = ()
# #创建单元素的元组
# one = (1,)
#获取元组的方法和list一样
# print(post)
# print(empty)
# print(one)
# print(post[0])
# print(post[-1])

#可变的元组
# 实现的方法是：元组里的元素为list,通过改变list间接的改变元组
post = ('产品部', '销售部', ['视频技术部', '视频运维部', '视频测试部'])
print(post)
videoPost = post[2]
videoPost[0] = '技术部'
videoPost[1] = '运维部'
videoPost[2] = '测试部'
print(post)
