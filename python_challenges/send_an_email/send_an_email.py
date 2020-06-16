# The challenge is to create a function that sends an email using python

# A solution is to use smtplib module. This is an SMTP protocol client

import smtplib

SENDER_EMAIL = 'example@gmail.com'
SENDER_PASSWORD = 'test12345'

def send_email(receiver_email,subject,body):
    message = f'Subject: {subject}\n\n{body}'

    with smtplib.SMTP_SSL('smtp@gmail.com',465) as server: #using smtplib
        server.login(SENDER_EMAIL,SENDER_PASSWORD) #login is an smtplib method
        server.sendmail(SENDER_EMAIL, receiver_email,message) #sendemail is an smtplib method

if __name__ == '__main__':
    print('This is the send an email tool using python')
    this_receiver = str(input('Type receiver email address:'))
    this_subject = str(input('Type your subject message now:'))
    this_body = str(input('Type your body message now:'))

    send_email(this_receiver,this_subject, this_body)
