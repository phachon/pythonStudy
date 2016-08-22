from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('home.html')


@app.route('/login', methods=['GET'])
def login_form():
	return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
	# 从request 对象读取表单内容
	username = request.form['username']
	password = request.form['password']

	if (username == 'admin' and password == '111111'):
		return render_template('home.html', message='登录成功', username=username)
	return render_template('login.html', message='登录失败')


if __name__ == '__main__':
	app.run()
