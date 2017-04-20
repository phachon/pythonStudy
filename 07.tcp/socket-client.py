"""
tcp 编程之客户端编程
"""
import socket

# 创建一个socket 连接，指定为 ipv4. tcp 流的方式连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接 tuple()
s.connect(('www.sina.com.cn', 80))
# 发送请求
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 开始接收数据
buffer = []
while True:
	# 每次接受 1k 字节
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

# 关闭连接'
s.close()

# 将 data 分离
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件
with open('sina.html', 'wb') as f:
	f.write(html)

