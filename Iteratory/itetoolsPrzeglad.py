import itertools
import operator

data = [1, 2, 3, 4, 5]


# accumulate sluzy, zeby na kazdym elemencie iterable obiektu(tutaj lista) wykonac operator.mul => czyli mnozenie
# czyli 1 *1, druga iteracja 1*1*2, trzecia, 1*1*2*3 itd
result = itertools.accumulate(data, operator.mul)

print(result)


for i in result:
    print(i)

print('-' * 50)


# count generuje liczby, pierwsza argument to liczba startowa
# drugi to o ile ma byc powiekszona wartosc
for i in itertools.count(10, 3):
    print(i)
    if i > 20:
        break

months = ["I", "II", "III", "IV", "V", "VI"]
# funkcja odopowiada za przechodzenie przez obiekt iterable w nieskonczonosc.
# for m in itertools.cycle(months):
#   print(m)

color_basic = ["red", "yellow", "blue"]
color_mix = ["green", "orange", "violet"]

# chain odpowiada za polczanenie dwoch obiektow w jeden(nie musza byc tego samego typu)
# nalezy pamietac, ze chain daje obiekt, ktory trzeba zdefiniowac np jako tuple, albo lista
result = itertools.chain(color_basic, color_mix)
print(tuple(result))

for i in result:
    print(i)

print('-'*30)


# compress sluzy do zwrocenia tylko i wylacznie elementy z pierwszego argumentu
# dla ktorych wartosci z drugiego argumentu sa rowne True
cars = ["Ford", "Opel", "Toyota", "Skoda"]
selections = [True, False, True, False]
result = itertools.compress(cars, selections)

for each in result:
    print(each)

print("-"*30)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]

# metoda sluzy do opuszczania elementow dopoki nie zostanie spelniony warunek(pierwszy argument)
result = itertools.dropwhile(lambda x: x < 5, data)

for i in result:
    print(i)

# to samo co dropwhile, z wyjatkiem, ze kazdy element jest poddawany warunkowi.
result = itertools.filterfalse(lambda x: x < 5, data)

for i in result:
    print(i)
# odwrotnosc dropwhile, generuje wszystkie liczby dajace False
result = itertools.takewhile(lambda x: x < 5, data)

for i in result:
    print(i)


months = ["I", "II", "III", "IV", "V", "VI"]
# wyciagnij elementy zaczynajac od elementu (3) i konczac na (5), bez uwzglednienia teog ostatniego
result = itertools.islice(months, 3, 6)
for i in result:
    print(i)


spades = ["Hearts", "Tiles", "Clovers", "Pikes"]
figures = ["Ace", "King", "Queen", "Jack", "10", '9']
# iloczyn kartezjanski, kazdy element drugiego obiektu jest przypisywany do kazdego elementu pierwszego
result = itertools.product(spades, figures)
print(list(result))

for i in result:
    print(i)


data = [(1, 2), (3, 4)]

# starmap potrzebuje obiektu zbudowanego z tuple w tuple albo np list w tuple itd
# sluzy do sumowania liczb znajdujacych sie w poszczegolych tuplach
result = itertools.starmap(operator.add, data)
for i in result:
    print(i)

cars = ["Ford", "Opel", "Toyota", "Skoda"]
# funkcja tee pozwala na stworzenie dowolnej ilosci iterator opierajacych sie na jednym obiekcie
# w jednej lini
cars1, cars2 = itertools.tee(cars)

for i in cars1:
    print(i)

print('-'*30)

for i in cars2:
    print(i)


months = ["Jan", "Feb", "Mar", "Apr", "May"]
plan = ['busy', 'busy',  'free', 'free']

# zip longest pozwala nam iterowac ze soba dwie listy bez wzgledu
# czy ich dlugosc jest taka sama, argumnet fillvalue pozwazala dopisywac
# do kolejnych elementow listy przekaczajacych dlugosc
result = itertools.zip_longest(months, plan, fillvalue="unknown")

for i in result:
    print(i)
