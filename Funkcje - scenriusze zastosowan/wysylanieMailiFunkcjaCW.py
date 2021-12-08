import smtplib

mailFrom = "zapchamcizlew@gmail.com"
mailTo = "karoolczak@gmail.com"
mailSubject = "Hello, this is bot"
mailBody = "This is bot of giving me money you dumb boy"

message = '''From:{}
Subject:{}
{}'''.format(mailFrom, mailSubject, mailBody)


user = "zapchamcizlew@gmail.com"
password = "Penumbra123"

try:

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message)
    print("Email sent")
except:
    print('error')
