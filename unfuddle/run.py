from unfuddle import Unfuddle
from settings import ACCOUNT_DETAILS
import json
from datetime import datetime, date, timedelta

unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])
trex_id = "37108"
accepted_tickets = []

# Display current projects
# print "Active Projects:"
# projects = unf.get_projects()
# for index, project in enumerate(projects):
#     print '%s. %s' % (index+1, project['title'])

# Get all active tickets from T-Rex
# Need to find a way to query the project ID
tickets = unf.get_tickets(trex_id)

with open('tickets.json', 'w') as outfile:
	json.dump(tickets, outfile)

# print '\n'
# print 'Active Tickets:'
# for ticket in tickets:
# 	if ticket['status'] == 'Accepted':
# 		#print datetime.strptime(ticket['updated_at'], '%Y-%m-%dT%H:%M:%SZ').date()
# 		#accepted_tickets.append(ticket)
# 		print ticket['summary']


# # Get the most recent comments. These will be update daily.
# current_time = datetime.today() - timedelta(days = 1)
# print '\n'
# print 'Recent Comments:'
# for ticket in tickets:
# 	if ticket.get('comments'):
# 		for comment in ticket['comments']:
# 			if datetime.strptime(comment['updated_at'], '%Y-%m-%dT%H:%M:%SZ') > current_time:
# 				print comment['body']
# 				print '-----------------------------------------------------------------'
