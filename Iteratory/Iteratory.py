import datetime as dt
import sys
from typing_extensions import ParamSpecArgs

# obiekty iterable to obiekty, ktore mozna przejsc petla for
# aby mozna bylo pobierac wartosci z iterable obiektu musimy miec iterator
# iterator to np klasa, funkcja
start = dt.datetime.now()
print("Execution started at {}".format(start))

# zapisz liste dat od 2000,1,1 co jeden dzien w range 2.5 kk
""" dates = [dt.date(2000, 1, 1) + dt.timedelta(days=1)for i in range(2500000)]
# getsizeof pokazuje ile zmienna w parametrze (dates) zuzyla pamieci operacyjnej
print("The size of list is:{} ".format(sys.getsizeof(dates)))
for d in dates:
    pass """
# STWORZENIE ITERATORA


class Miliondays():
    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    # __next__ to metoda do iterowania, wywoluje sie ja jak yield, czyli nextem
    # tutaj definiujemy petle
    def __next__(self):
        if self.maxdays < 1:  # jezeli zmienna maxdays bedzie mniejsza od 1
            raise StopIteration()  # zatrzymaj iteracje
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1  # z kazdym dodaniem daty do self.date zmniejszamy zmienna maxdays o 1
        return ret
    # funkcja do stworzenia iteratora, ktory zostal zaimplementowany w funkcji __next__
    # __next__ i __iter__ zawsze musze byc razem

    def __iter__(self):
        return self


""" 
md = Miliondays(2000, 1, 1, 2500000)
print("Size of md: {}".format(sys.getsizeof(md)))
# wywolanie metody __next__ wywoluje sie jak yield
print(next(md))
print(next(md))
# petla z uzyciem metody oraz
for i in range(md.maxdays):
    next(md)


 """
md = Miliondays(2000, 1, 1, 2500000)
print("Size of md: {}".format(sys.getsizeof(md)))
for d in md:
    pass


stop = dt.datetime.now()
print("Execution stoped at {}".format(stop))

print("Total time {}".format(stop - start))
