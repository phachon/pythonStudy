from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
	return '<form action="/signin" method="post">' \
			'<p>用户名：<input type="text" value="" name="username"></p>' \
			'<p>密码：<input type="password" name="password" id=""></p>' \
			'<p><button type="submit">SignIn</button></p>' \
			'</form>'


@app.route('/signin', methods=['POST'])
def signin():
	# 从request 对象读取表单内容
	username = request.form['username']
	password = request.form['password']
	
	if(username == 'admin' and password == '111111'):
		return '<h1>登陆成功</h1>'
	return '<h1>登陆失败</h1>'

if __name__ == '__main__':
	app.run()
