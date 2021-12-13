import itertools as it


filepath = r"D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Generatory\data.txt"

data = []

with open(filepath)as file:
    for line in file:
        # rozbij elements na elementy(tuple) miedzy znakiem ':'
        elements = line.rstrip("\n").split(':')
        # slownik
        d = {"type": elements[0], "action": elements[1]}
        data.append(d)

# wyznaczanie ile bylo typow danych zdarzen
myList = []


# posortowanie data wzgledem klucz przypisanych do type
# lambda x: x['type'] = przypisanie kazdego elementu do klucza "type"
data = sorted(data, key=lambda x: x['type'])


# The groupby() function takes two arguments: (1) the data to group
#  and (2) the function to group it with.
# Here, lambda x: x[0] tells groupby() to use
# the first item in each tuple/dictionary as the grouping key.
for key, elements in it.groupby(data, key=lambda x: x['type']):
    print("{} - {}" .format(key, len(list(elements))))
