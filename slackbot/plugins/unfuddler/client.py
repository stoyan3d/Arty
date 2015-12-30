from unfuddle import Unfuddle
from settings import ACCOUNT_DETAILS
import os
import json
import logging
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)

class Client(object):
	def __init__(self):
		self.unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])
		self.trex_id = '37108'
		self.ticket_url = self.unf.base_url + '/a#/projects/' + self.trex_id + '/tickets/by_number/'
		self.downloads = 'D:/Temp/'

	def get_active(self):
		# Get all active tickets from T-Rex
		logger.info('Getting active tickets.')
		active_tickets = []
		index = 1
		tickets = self.unf.get_tickets(self.trex_id)
		for ticket in tickets:
			if ticket['status'] == 'Accepted':
				active_tickets.append(str(index) + '. ' + ticket['summary'] + '\n' 
					+ self.ticket_url + str(ticket['number']))
				index += 1
		return active_tickets

	def get_comments(self):
		# Get the most recent comments with their attachments. These will be updated daily.
		logger.info('Getting recent comments.')
		recent_comments = []
		recent_attachments = {'comment' : None, 'attachments' : None}
		tickets = self.unf.get_tickets(self.trex_id)
		current_time = datetime.today() - timedelta(days = 1)
		for ticket in tickets:
			# Some tickets tend to not have comments
			if ticket.get('comments'):
				for comment in ticket['comments']:
					if datetime.strptime(comment['updated_at'], '%Y-%m-%dT%H:%M:%SZ') > current_time:

						recent_comments.append(comment['body'])
						if comment.get('attachments'):
							for attachment in comment['attachments']:
								# Create unique path for each download
								self.unf.get_attachments(self.trex_id, ticket['id'], comment['id'], attachment['id'], attachment['filename'])

		return recent_comments


	def print_something(self):
		logger.info("I'm alive on Python.")
		return "I'm alive on Slack."

	def download(self):
		download_path = '5454\\stuff\\'
		path = os.path.join(os.getcwd(), download_path)
		if not os.path.exists(path):
			os.makedirs(path)
		self.unf.get_attachments(self.trex_id, 582458, 458997, 190940, path + 'something.zip')