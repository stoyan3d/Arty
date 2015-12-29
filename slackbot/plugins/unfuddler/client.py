from unfuddle import Unfuddle
from settings import ACCOUNT_DETAILS
import json
import urllib2
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
		# Get the most recent comments. These will be updated daily.
		logger.info('Getting recent comments.')
		recent_comments = []
		tickets = self.unf.get_tickets(self.trex_id)
		current_time = datetime.today() - timedelta(days = 1)
		for ticket in tickets:
			# Some tickets tend to not have comments
			if ticket.get('comments'):
				for comment in ticket['comments']:
					if datetime.strptime(comment['updated_at'], '%Y-%m-%dT%H:%M:%SZ') > current_time:
						#print comment['body']
						recent_comments.append(comment['body'])
		return recent_comments


	def print_something(self):
		logger.info("I'm alive on Python.")
		return "I'm alive on Slack."

	def download(self):
		#response = urllib2.urlopen('https://gameshastra.unfuddle.com/projects/37108/tickets/582458/comments/458997/attachments/190940/download', self.downloads + 'something.zip')
		#html = response.read()
		self.unf.get('projects/37108/tickets/582458/comments/458997/attachments/190940/download')