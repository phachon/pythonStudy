#server.py
from wsgiref.simple_server import make_server
from hello import application

# 创建一个server
httpd = make_server('', 8000, application)
print('Server Http on port 8000')
# 开始监听http请求
httpd.serve_forever()
