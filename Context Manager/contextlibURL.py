# biblioteka odpowiadajaca za sciagniecie zawartosci strony internetowej
from urllib.request import urlopen
from contextlib import closing

# Dzieki bibliotece closing, obiekt zamyka sie samemu.
with closing(urlopen('http://www.kursyonline24.eu')) as page:
    for line in page:
        print(line)
