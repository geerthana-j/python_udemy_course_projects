import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "geerthana.cs19@bitsathy.ac.in"
    password = "Gathu@01"

    receiver = "geerthikumar2100@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)