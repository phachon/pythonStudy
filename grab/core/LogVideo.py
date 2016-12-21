"""
video 抓取日志
@author panchao
@time 2016-08-31
"""
from grab.core.DB import DB


class LogVideo(object):

	level_info = '0'
	level_waring = '1'
	level_error = '2'
	level_debug = '3'

	def __init__(self, level):
		self._level = level

	def write(self, urlId, message, extra, grabVideoId=0, videoId=0):
		data = {
			'level': self._level,
			'url_id': urlId,
			'message': message,
			'extra': extra,
			'grab_video_id': grabVideoId,
			'video_id': videoId,
		}
		db = DB()
		db.insert('grab_log_video').columns(data.keys()).values(data.values()).execute('grab_video').rowCount()