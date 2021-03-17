import secrets
import string
from twilio.rest import Client


account_sid = 'AC0c35e9b0420ada8acd522d46a7a9dfc6'
auth_token = '381d69aa486be78150a839222615d906'
client = Client(account_sid, auth_token)
segredo = string.digits
senha = ''.join(secrets.choice(segredo) for i in range(4))
message = client.messages \
                .create(
                     body="codigo de validação : "+senha,
                     from_='+17062233376',
                     to='+5511986284682'
                 )

print(message.sid)