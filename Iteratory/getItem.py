import datetime as dt


class Miliondays():
    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays
    # item okresla ktora wartosc ma byc wygenerowana

    def __getitem__(self, item):
        if item <= self.maxdays:
            # days = item => wskazanie jaki dzien chcemy
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()


md = Miliondays(2000, 1, 1, 35)

print(md[0], md[1])

# jezeli klasa spelnia wymagania, aby byc iterable(czyli byc w petli for)

# generowanie sztucznego iteratora
# poniewaz klasa nie jest zadeklarowana jako iterator(nie ma __next__)
it = iter(md)
print(next(it))
print(next(it))
print(next(it))

for i in md:
    print(i)
