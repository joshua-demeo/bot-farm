import smtplib
import ssl
from email.message import EmailMessage

from local_secrets import SENDER_EMAIL, SENDER_PASSWORD

def send_email(receiver_email, subject, message):
    '''General function to send emails via gmail account'''
    
    port = 465
    host = "smtp.gmail.com"

    # Create payload
    payload = EmailMessage()
    payload['From'] = SENDER_EMAIL
    payload['To'] = receiver_email
    payload['Subject'] = subject
    payload.set_content(message)
    print(payload)

    # Connect to SMTP server and send message
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        print('Sending Email...')
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(payload)