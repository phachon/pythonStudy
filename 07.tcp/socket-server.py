"""
tcp 编程之服务器端编程
"""
import socket
import time
import threading


# 创建一个 socket 连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
s.bind(('127.0.0.1', 8099))

# 监听端口(最大连接数)
s.listen(5)
print("正在监听端口....")


# 处理请求
def tcplink(sock, address):
	print("接收一个新的连接来自 %s:%s..." % address)
	sock.send(b'welcome!')
	# 接收数据
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	# 关闭sock
	sock.close()
	print("连接来自 %s:%s 已关闭" % address)

# 阻塞等待处理请求
while True:
	# 接收一个新连接
	sock, address = s.accept()
	# 创建新线程处理 tcp 连接
	t = threading.Thread(target=tcplink, args=(sock, address))
	# 线程开启
	t.start()
