from twilio.rest import Client

def enviar_sms(telefone,senha):
    account_sid = 'AC0c35e9b0420ada8acd522d46a7a9dfc6'
    auth_token = 'cd697d43989b22b496249b4b8c84f070'
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="codigo de validação : "+senha,
                         from_='+17062233376',
                         to= telefone
                     )
    return message.sid
