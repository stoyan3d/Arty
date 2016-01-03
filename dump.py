# Dumps all tickets in a project into a Json file

import json
from datetime import datetime, date, timedelta
from slackbot.plugins.unfuddler.unfuddle import Unfuddle
from slackbot.plugins.unfuddler.settings import ACCOUNT_DETAILS

unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])
trex_id = "37108"

tickets = unf.get_tickets(trex_id)

with open('tickets.json', 'w') as outfile:
	json.dump(tickets, outfile, sort_keys = True, indent = 4, separators = (',', ': '))