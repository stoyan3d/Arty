from unfuddle import Unfuddle
from settings import ACCOUNT_DETAILS
import json
from datetime import datetime, date, timedelta

class Client(object):
	def __init__(self):
		self.unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])

	def get_active(self):
		# Get all active tickets from T-Rex
		trex_id = "37108"
		tickets = self.unf.get_tickets(trex_id)
		print '\n'
		print 'Active Tickets:'
		for ticket in tickets:
			if ticket['status'] == 'Accepted':
				print ticket['summary']


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
		print str(datetime.today()) + " I'm alive on Python."
		return "I'm alive on Slack."
