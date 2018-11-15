"""
urllib parse url
"""
from urllib import parse

url = ""

parseResult = parse.urlparse(url)
param_dict = parse.parse_qs(parseResult.query)

print(param_dict)

for key in param_dict:
	print(key)
	print(param_dict[key])
	# print(value)
