from unfuddle import Unfuddle
from settings import ACCOUNT_DETAILS

unf = Unfuddle(ACCOUNT_DETAILS["account"], ACCOUNT_DETAILS["username"], ACCOUNT_DETAILS["password"])

report_title = "My Active Tickets"
reports = unf.get_ticket_reports()
my_active_tickets_report, = [r for r in reports if report_title in r['title']]
report = unf.generate_ticket_report(my_active_tickets_report['id'])
for group in report['groups']:
    print group['title']
    for t in group['tickets'][:5]:
        print "%s %s" % (t['number'], t['summary'])
    print