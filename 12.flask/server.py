from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)


@app.route('/author', methods=['GET'])
def author():
	return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
	username = request.args.get['username']
	# username = request.form['username']
	password = request.form['password']

	return username

if __name__ == '__main__':
	app.run(debug=True)
