
from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
client.messages.create(
  to="",
  from_="",
  body="Oi :)",
  media_url="https://climacons.herokuapp.com/clear.png")