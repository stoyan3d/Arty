from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.plugins.unfuddler.unfuddle import Unfuddle
from slackbot.plugins.unfuddler.settings import ACCOUNT_DETAILS
import os
import shutil
import logging
import re
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)

unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])
trex_id = '37108'
ticket_url = unf.base_url + '/a#/projects/' + trex_id + '/tickets/'

@listen_to('active tickets', re.IGNORECASE)
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
def get_comments(message):
	# Get the most recent comments with their attachments. These will be updated daily.
	message.reply('There are some updates:')
	logger.info('Getting recent comments.')
	tickets = unf.get_tickets(trex_id)
	current_time = datetime.today() - timedelta(days = 1)
	for ticket in tickets:
		# Some tickets tend to not have comments
		if ticket.get('comments'):
			for comment in ticket['comments']:
				if datetime.strptime(comment['updated_at'], '%Y-%m-%dT%H:%M:%SZ') > current_time:
					message.send(str(index) + '. ' + ticket['summary'] + ' Ticket ID is: ' + str(ticket['id']) + '\n' 
						+ ticket_url + str(ticket['id']))
					message.send(comment['body'])
					if comment.get('attachments'):
						for attachment in comment['attachments']:
							# Create unique path for each download
							download_path = 'downloads\\%d\\%d\\' % (ticket['id'], comment['id'])
							path = os.path.join(os.getcwd(), download_path)
							if not os.path.exists(path):
								os.makedirs(path)
							unf.get_attachments(trex_id, ticket['id'], comment['id'], attachment['id'], path + attachment['filename'])
							message.channel.upload_file(attachment['filename'], path + attachment['filename'])
							
@respond_to('delete downloads', re.IGNORECASE)
def delete_downloads(message):
	rempath = os.path.join(os.getcwd(), 'downloads\\')
	logger.info('Deleting files from ' + rempath)
	message.reply('Deleting all downloaded files.')
	shutil.rmtree(rempath)

@listen_to('update comment')
def update_ticket(message):
	message.send('Creating comment.')
	logger.info('Updating ticket.')
	#print 'URL is:'
	#print url
	#comment = url[6:]
	#print 'Comment is:'
	#print comment
	#ticket_number = url[3:5]
	#print 'Ticket numer is:'
	#print ticket_number
	
	#message.reply('Updating ticket number %s with the comment: %s.' %(ticket_number, comment))
	unf.comment_ticket(trex_id, '582487', {'body' : 'Commented from a bot.'})