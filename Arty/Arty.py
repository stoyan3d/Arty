import time
from slackclient import SlackClient
#import slackclient from SlackClient

# This token value needs to be external for security reasons
token = "xoxb-17298431846-I8i5T6PolMevx527rEPZqozM" # found at https://api.slack.com/web#authentication
sc = SlackClient(token)
channel = "#arty-test"
greeting = "Hello folks, I'm online!"

if sc.rtm_connect():
    sc.rtm_send_message([channel, "greeting"])
    while True:
        print(sc.rtm_read())
        time.sleep(1)
else:
    print("Connection failed!")