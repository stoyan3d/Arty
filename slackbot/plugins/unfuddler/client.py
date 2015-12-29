from unfuddle import Unfuddle
from settings import ACCOUNT_DETAILS
import json
import logging
from datetime import datetime, date, timedelta

logger = logging.getLogger(__name__)

class Client(object):
	def __init__(self):
		self.unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])

	def get_active(self):
		# Get all active tickets from T-Rex
		logger.info ('Getting active tickets.')
		active_tickets = []
		index = 1
		trex_id = "37108"
		ticket_url = self.unf.base_url + '/a#/projects/' + trex_id + '/tickets/by_number/'
		tickets = self.unf.get_tickets(trex_id)
		for ticket in tickets:
			if ticket['status'] == 'Accepted':
				active_tickets.append(str(index) + '. ' + ticket['summary'] + '\n' 
					+ ticket_url + str(ticket['number']))
				index += 1
				#print ticket['summary']
		return active_tickets


# Get the most recent comments. These will be update daily.
	def get_comments(self):
		trex_id = "37108"
		tickets = self.unf.get_tickets(trex_id)
		current_time = datetime.today() - timedelta(days = 1)
		print '\n'
		print 'Recent Comments:'
		for ticket in tickets:
			if ticket.get('comments'):
				for comment in ticket['comments']:
					if datetime.strptime(comment['updated_at'], '%Y-%m-%dT%H:%M:%SZ') > current_time:
						print comment['body']
						print '-----------------------------------------------------------------'

	def print_something(self):
		logger.info("I'm alive on Python.")
		return "I'm alive on Slack."
