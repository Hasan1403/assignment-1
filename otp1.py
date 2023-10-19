from twilio.rest import Client
import math
import random
import smtplib
account_sid = 'AC133b5611dc2f564f9a9409480360b343'
auth_token = '19c04ea6bdafbe2ddc64d99248d2c1b3'

twilio_number = '+17203994797'
target_number = ''
client = Client(account_sid,auth_token)
digits="0123456789" 
otp=""
for i in range(6): 
    otp+=digits[math.floor(random.random()*10)] 
otp = otp + " is your otp" 
msg= otp
message = client.messages.create(
    body = msg,
    from_ = twilio_number,
    to = '+918080763621'
)
print(message.body)

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('jahirhasankureshi@gmail.com','pkxfxwmurndkgzkt')
msg='HELLO YOUR OTP IS '+str(otp)
server.sendmail('jahirhasankureshi@gmail.com','naikatharva1111@gmail.com',msg)
server.quit()