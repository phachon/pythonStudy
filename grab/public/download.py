"""
下载
@author panchao
@time 2016-08-31
"""
from grab.bass.bass_url import BassUrl
from grab.core.LogVideo import LogVideo
import os

# 查找未下载的 url
grabUrls = BassUrl().getDefaultUrls()
if len(grabUrls) == 0:
	exit()
else:
	for grabUrl in grabUrls:
		url = grabUrl['url']
		urlId = grabUrl['url_id']
		cmd = 'you-get --url --json %s' % url

		# log
		#LogVideo(LogVideo.level_info).write(urlId, '抓取url开始', cmd)

		result = os.popen(cmd)
		print(result)
		exit()



