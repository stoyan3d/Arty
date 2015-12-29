from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.plugins.unfuddler.client import Client
import re

unf = Client()

@listen_to('active tickets', re.IGNORECASE)
def unfuddle_send(message):
	message.reply('Here are the currently active tickets:')
	active_tickets = unf.get_active()
	for i in active_tickets:
		message.send(i)