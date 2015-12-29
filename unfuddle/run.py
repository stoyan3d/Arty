from unfuddle import Unfuddle
from settings import ACCOUNT_DETAILS
import json

unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])

accepted_tickets = []

# Display current projects
print "Active Projects:"
projects = unf.get_projects()
for index, project in enumerate(projects):
    print '%s. %s' % (index+1, project['title'])

# Get all active tickets from T-Rex
# Need to find a way to query the project ID
tickets = unf.get_tickets("37108")

# with open('tickets.json', 'w') as outfile:
# 	json.dump(tickets, outfile)
print 'Active Tickets:'
for ticket in tickets:
	if ticket['status'] == 'Accepted':
		#accepted_tickets.append(ticket)
		print ticket['summary']