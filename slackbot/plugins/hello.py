from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re

# The decrators are similar to re.compile('hello$', re.IGNORECASE)

@respond_to('hello|hi', re.IGNORECASE)
def hello_reply(message):
    message.reply('hello dude!')


@listen_to('hello|hi')
def hello_send(message):
    message.send('hello all!')

@listen_to('awesome|amazing|great work|nice|cool')
def best_send(message):
	message.send("Best one yet!")


@listen_to('hello_decorators')
@respond_to('hello_decorators')
def hello_decorators(message):
    message.send('hello!')
