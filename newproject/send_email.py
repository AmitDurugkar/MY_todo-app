import smtplib ,ssl

def Send_email(massage):
    host = "smtp.gmail.com"
    port = 465
    username = "amit.durugkar@gmail.com"
    password = "iltm exhx cuyb bxhd "
    receiver = "amit.durugkar@gmail.com"
    context = ssl.create_default_context()
    massage = """ \
    Subject : Hi! 
    How are you 
    Bye  """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, massage)

