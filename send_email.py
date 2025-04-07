import smtplib, ssl, os

# Using Python to send an email from Gmail.
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    password = os.getenv("Pass")
    username = "dylanroach648@gmail.com"

    receiver = "dylanroach648@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
