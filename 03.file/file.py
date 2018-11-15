#f = open('test.txt', 'w');

#只读，必须存在
f = open('test.txt', 'r');
#只写，不存在则创建
f = open('test.txt', 'w');
#追加
f = open('test.txt', 'a');
#读写方式
f = open('test.txt', 'r+');
#读写 会清空文件
f = open('test.txt', 'w+');

infos = f.readline();

for info in infos:
	print(info);
f.close();