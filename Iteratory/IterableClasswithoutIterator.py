import datetime as dt

# klasa iterator, ale sama w sobie nie jest iterable


class MiliondaysIterator():

    def __init__(self, date, max):
        self.date = date
        self.maxdays = max

    # __next__ to metoda, ktora tworzy iterator
    def __next__(self):
        if self.maxdays < 0:  # jezeli zmienna maxdays bedzie mniejsza od 1
            raise StopIteration()  # zatrzymaj iteracje
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1  # z kazdym dodaniem daty do self.date zmniejszamy zmienna maxdays o 1
        return ret

# klasa jest iterable, ale nie posiada wlasnego iteratora


class Miliondays():
    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays
        # zmienna wskazujaca na obiekt MiliondaysIterator z jego parametrami
        self.iterator = MiliondaysIterator(self.date, self.maxdays)

    # __iter__ wskazuje, ze klasa jest iterable
    # __next__ i __iter__ zawsze musze byc razem
    def __iter__(self):
        return self.iterator  # odwoluje sie do obiektu klasy MiliondaysIterator


md = Miliondays(2000, 1, 1, 2)
for d in md:
    print(d)
