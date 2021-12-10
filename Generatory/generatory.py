import datetime as dt

# Generator to funkcja


def Miliondays(year, month, day, maxdays):
    date = dt.date(year, month, day)
    for i in range(maxdays):
        yield (date + dt.timedelta(days=i))


md = Miliondays(2000, 1, 1, 3)
for d in md:
    print(d)


def getNumber():
    yield(24)
    yield(23)
    yield(21)
    yield(3)
    yield(8)


i = getNumber()

print(next(i))
print(next(i))
print(next(i))
print(next(i))
