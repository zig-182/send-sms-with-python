# Install Twilio if you haven't already. Check README for more info

from twilio.rest import Client

# Replace the following placeholders with your actual Twilio credentials
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

message = client.messages.create(
  # Replace with your Twilio Number
  from_='+44 XXX XXXXXX',
  
  # Replace with the number you'll send it to
  to='+44 XXXX XXXXXX',
  
  # Message content
  body="MESSAGE"
 )
# The unique identifier (SID) of the sent message
print(message.sid)