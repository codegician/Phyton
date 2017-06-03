from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC62658916bf5b98593130a894e105bcc1"
# Your Auth Token from twilio.com/console
auth_token  = "9f1d098f395e7ad7bce7926d00cd4d9c"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12064225393", 
    from_="+12064830395",
    body="Dark")

print(message.sid)
