import smtplib
import functools


def sendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = '''From: {}
Subject:{}
{}

'''.format(mailFrom, mailSubject, mailBody)

    try:
        # smtp_ssl= klient jakiego oczekuje google
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()  # Przesylanie podstawowych informacji o PC z ktorego wychodzi polaczenie z serwerem poczty
        server.login(user, password)  # zalogowanie sie do maila
        # wyslanie(adres z ktorego wysylam, adres do ktorego, wiadomosc)
        server.sendmail(user, mailTo, message)
        server.close()  # zamkniecie polaczenia
        print("Mail sent")
        return("Mail sent")
    except:
        return("error")


user = "zapchamcizlew@gmail.com"
password = 'Penumbra123'
mailFrom = "Your automation system"  # skad mail
mailTo = "karoolczak@gmail.com"
mailSubject = "Processing finish successfully"
mailBody = "Hello, have a nice day"

# argumeny (funkcja, parametry, ktore funkcja powinna juz znac)
SendInfoEmailFromGmail = functools.partial(
    sendInfoEmail, user, password,)

# zmienna za pomoca ktorej wywoluje funkcje do wyslania maila
# argumenty musza byc wysylane po kolei !
SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody, )


#sendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
