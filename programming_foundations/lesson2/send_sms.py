import os
from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACef69d158207822160e5c408f6fbb95ff"
auth_token  = os.getenv('TWILIO_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="This is awesome!",
    to="+1",    # Replace with your phone number
    from_="+16509461521") # Replace with your Twilio number
print message.sid