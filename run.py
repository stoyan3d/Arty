from slacker import Slacker

slack = Slacker("xoxb-17298431846-I8i5T6PolMevx527rEPZqozM")

channel = "#arty-test"
message = "Hello happy people"

slack.chat.post_message(channel, message, as_user = True)