from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


class Router(object):

	def __init__(self):
		pass

	@app.route('/hello/')
	@app.route('/hello/<name>')
	def hello(name=None):
		return render_template('/app/templates/hello.html', name=name)


if __name__ == '__main__':
	app.run(debug=True)
