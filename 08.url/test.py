"""
urllib 的例子
"""
import urllib.request

fp = urllib.request.urlopen('http://www.baidu.com')
myBytes = fp.read()

myStr = myBytes.decode("utf8")
fp.close()
print(myStr)
