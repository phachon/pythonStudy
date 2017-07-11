"""
加载配置信息
"""
import os

root_dir = os.path.dirname(os.path.abspath(rabbitmq.__file__))

def load():
	root  = os.path