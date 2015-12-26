from artybot import settings
from slacker import Slacker

class Bot(object):
	def __init__(self):
		self._client = Slacker(settings.API_TOKEN)

	def run(self):
		#self._client.rtm_connect()
		channel = "#arty-test"
		message = "Hello happy people"
		self._client.chat.post_message(channel, message, as_user = True)