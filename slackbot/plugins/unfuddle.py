from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.plugins.unfuddler.client import Client
import re

unf = Client()

@listen_to('active tickets', re.IGNORECASE)
def unfuddle_tickets(message):
	message.reply('Here are the currently active tickets:')
	active_tickets = unf.get_active()
	for i in active_tickets:
		message.send(i)

@listen_to('recent comments', re.IGNORECASE)
def unfuddle_comments(message):
	message.reply('There are some updates:')
	recent_comments = unf.get_comments()
	for c in recent_comments:
		message.send(c)

@listen_to('download', re.IGNORECASE)
def download(message):
	message.reply('Downloading files')
	unf.download()