from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.plugins.unfuddler.client import Client
import re

unf = Client()

@listen_to('unf|unfuddle', re.IGNORECASE)
def unfuddle_send(message):
	message.reply('Here are some Unfuddle tickets for you!')
	text = unf.print_something()
	text2 = ["stuff", "more stuff"]
	for i in text2:
		message.send(i)