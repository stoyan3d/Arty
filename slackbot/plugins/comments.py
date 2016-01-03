import os
import shutil
import logging
import re
import random
import time
from datetime import datetime, date, timedelta
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.plugins.unfuddler.unfuddle import Unfuddle
from slackbot.plugins.unfuddler.settings import ACCOUNT_DETAILS

logger = logging.getLogger(__name__)

unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])
trex_id = '37108'
stoyan_id = 50705
natalie_id = 50734
ticket_url = unf.base_url + '/a#/projects/' + trex_id + '/tickets/'
update_time = 60 # In minutes

@respond_to('active tickets', re.IGNORECASE)
def get_active(message):
	# Get all active tickets from T-Rex
	message.reply('Here are the currently active tickets:')
	logger.info('Getting active tickets.')
	active_tickets = []
	index = 1
	tickets = unf.get_tickets(trex_id)
	for ticket in tickets:
		if ticket['status'] == 'Accepted':
			message.send(str(index) + '. ' + ticket['summary'] + ' Ticket ID is: ' + str(ticket['id']) + '\n' 
				+ ticket_url + str(ticket['id']))
			index += 1

@listen_to('recent updates', re.IGNORECASE)
# TODO: get latest Gameshastra comment for each active ticket
# Check for this every hour and ping relevant people
def get_comments(message):
	# Get the most recent comments with their attachments. These will be updated daily.
	message.reply('There are some updates:')
	logger.info('Getting recent comments.')
	tickets = unf.get_tickets(trex_id)
	current_time = datetime.today() - timedelta(days = 3)
	print current_time
	index = 1
	while True:
		for ticket in tickets:
			# Some tickets tend to not have comments
			if ticket.get('comments') and ticket['status'] == 'Accepted':
				#for comment in ticket['comments']:
					#if datetime.strptime(comment['updated_at'], '%Y-%m-%dT%H:%M:%SZ') > current_time:
				if (ticket['comments'][-1]['author_id'] != stoyan_id and ticket['comments'][-1]['author_id'] != stoyan_id):
					#message.send(comment['updated_at'])
					message.send(str(index) + '. ' + ticket['summary'] + ' Ticket ID is: ' + str(ticket['id']) + '\n' 
						+ ticket_url + str(ticket['id']))
					index += 1
					message.send(ticket['comments'][-1]['body'])
					if ticket['comments'][-1].get('attachments'):
						for attachment in ticket['comments'][-1]['attachments']:
							# Create unique path for each download
							download_path = 'downloads\\%d\\%d\\' % (ticket['id'], ticket['comments'][-1]['id'])
							path = os.path.join(os.getcwd(), download_path)
							if not os.path.exists(path):
								os.makedirs(path)
							unf.get_attachments(trex_id, ticket['id'], ticket['comments'][-1]['id'], attachment['id'], path + attachment['filename'])
							message.channel.upload_file(attachment['filename'], path + attachment['filename'])
		time.sleep(update_time*60)

@respond_to('delete downloads', re.IGNORECASE)
def delete_downloads(message):
	rempath = os.path.join(os.getcwd(), 'downloads\\')
	logger.info('Deleting files from ' + rempath)
	message.reply('Deleting all downloaded files.')
	shutil.rmtree(rempath)

@respond_to(r'feedback re:(\d{6})(.*)')
def update_ticket(message, ticket_id, reply):
	message.send('Creating comment.')
	logger.info('Updating ticket.')
	intro = 'Hello, \n'
	body = [
	'Looks good! Please move on to the next stage.',
	'No feedback from us, it looks great!',
	'Excellent work! Looking forward to the next stage.'
	]
	outro = '\nThanks,\nStoyan'
	comment = intro + random.choice(body) + outro

	reply = reply[1:]
	if reply == 'approved':
		message.reply('Updating ticket number %s with the comment:\n%s.' %(ticket_id, comment))
		unf.post_comment(trex_id, ticket_id, {'body' : comment})
	else:
		message.reply('Not valid feedback.')

# @listen_to('https://(.*)')
# def download_files(message, url):
# 	message.send('Yup, there is something to download: %s' %url)
