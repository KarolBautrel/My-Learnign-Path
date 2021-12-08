import smtplib

mailFrom = "Your automation system"  # skad mail
mailTo = "karoolczak@gmail.com"
mailSubject = "Processing finish successfully"
mailBody = "Hello, have a nice day"

message = '''From: {}
Subject:{}
{}

'''.format(mailFrom, mailSubject, mailBody)

user = "zapchamcizlew@gmail.com"
password = 'Penumbra123'


try:
    # smtp_ssl= klient jakiego oczekuje google
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()  # Przesylanie podstawowych informacji o PC z ktorego wychodzi polaczenie z serwerem poczty
    server.login(user, password)  # zalogowanie sie do maila
    # wyslanie(adres z ktorego wysylam, adres do ktorego, wiadomosc)
    server.sendmail(user, mailTo, message)
    server.close()  # zamkniecie polaczenia
    print("Mail sent")
except:
    print("error")
