
from tornado.web import RequestHandler as BaseRequestHandler, HTTPError

class BaseHandler(BaseRequestHandler):
    def get(self, *args, **kwargs):
        # enable GET request when enable delegate get to post

    def prepare(self):
        self.traffic_control()
        pass

    def traffic_control(self):
        # traffic control hooks for api call etc
        self.log_apicall()
        pass

    def log_apicall(self):
        pass

class MqHandle(BaseHandler):
	def get(self, *args, **kwargs):
