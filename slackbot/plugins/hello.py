from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

# The decrators are similar to re.compile('hello$', re.IGNORECASE)

@listen_to('hello|hi', re.IGNORECASE)
def hello_send(message):
    message.send('hello!')

@listen_to('awesome|amazing|great work|nice|cool', re.IGNORECASE)
def best_send(message):
	message.send("Best one yet!")