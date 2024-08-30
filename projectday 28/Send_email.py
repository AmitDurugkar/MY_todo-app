import os
import smtplib ,ssl

def send_email(massage):
    host = "smtp.gmail.com"
    port = 465
    username = "amit.durugkar@gmail.com"
    password = os.getenv("PASSWORD ")

    receiver = "amit.durugkar@gmail.com"
    context = ssl.create_default_context()
    massage = """ \
    Subject : Hi! 
    How are you 
    Bye  """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, massage)