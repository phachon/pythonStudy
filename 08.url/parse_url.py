"""
urllib parse url
"""
from urllib import parse

url = "http://api.weibo.cn/2/guest/cardlist?fid=1076036361672873_-_WEIBO_SECOND_PROFILE_WEIBO&uid=1005419921135&lfid=100303type%3D1%26t%3D3&checktoken=58f0a3718c98bef2b2273174202f34de&count=20&extparam=&from=1051095013&lang=zh_CN&lcardid=user&skin=default&gsid=_2AkMgAcs7f8NhqwJRmP0RzWLrbox2yQ3EiebDAHrsJxIwHnE17DxnqF9rySCUONhK7dCBp-JElMhh53Ws&page=1&containerid=1076036361672873_-_WEIBO_SECOND_PROFILE_WEIBO&oldwm=8605_2003&v_p=17&v_f=2&c=android&wm=8605_2003&did=8614fefc3b0ce17aa11802c261867f61853e8274&luicode=10000003&i=f315bfe&s=c9a46cc7&ua=HUAWEI+G610-U00__weibo__5.1.0__android__android4.2.2&uicode=10000198&imsi=&featurecode=10000085"

parseResult = parse.urlparse(url)
param_dict = parse.parse_qs(parseResult.query)

# print(param_dict)

for key in param_dict:
	val = ','.join(param_dict[key])
	print(key+":"+ val)
