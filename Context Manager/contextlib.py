from contextlib import redirect_stdout
from contextlib import suppress
from contextlib import contextmanager
import os


class Door:

    def __init__(self, where):
        self.where = where

    def open(self):
        print("Opening door to the {}".format(self.where))

    def close(self):
        print("Closing door to the {}".format(self.where))


#door1 = Door("Hell")
#door2 = Door("future")


# aby nie modyfikowac funkcji tworzymy nowa, ktora jest generatorem.
# argumentem funkcji jest kazdy element klasy ktore implementuje metode open i close
@contextmanager
def openAndClose(obj):
    obj.open()
    yield obj
    obj.close()
# z racji tego ze generator po wykonaniu iteracji zamraza obiekt
# to jest to okazja, aby ten obiekt z generatora wyciagnac i cos z nim zrobic
# uzyc go w wyrazeniu with, kiedy wyrazenie with sie zakonczy, to obiekt wraca do
# generatora i wykonuje kolejna funkcje (close )


# do with implementujemy funkcje openAndClose, zeby zakomunikowac, ze chcemy sie przelaczac do tej funkcji
# musimy funkcje dolaczona do with udekorowac contextmanager
# musimy uzyc biblioteki contextlib

with openAndClose(Door("next room")) as door:
    print("The door is to the {}".format(door.where))


# zamiana funkcji na taka, ktora tylko zamyka drzwi, ktore sami otiweramy

print("-"*30)


@contextmanager
def onlyClose(obj):
    yield obj
    obj.close()


with onlyClose(Door("next room")) as door:
    door.open()
    print("The door is to the {}".format(door.where))


#os.remove(r"D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager\asd")
# dzieki bibliotece mozemy zrobic wyjatek (Jak try/except, dzieki ktoremu program nie zostanie przerwany)
with suppress(FileNotFoundError):
    os.remove(
        r"D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager\asd")

# redirect_stdout sluzy do przekierowania outputu do pliku
f = open(r"D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager\log.txt", "w")
with redirect_stdout(f):
    print("Hello")
    d = Door('Exit')
    d.open()
