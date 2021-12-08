from typing import Counter


ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

generator = ((start, stop)
             for start in ports for stop in ports if start != stop)
newList = []
for elements in generator:
    newList.append(elements)

print(len(newList))


# ALBO TAK
generator = ((start, stop)
             for start in ports for stop in ports if start != stop)
counter = 0
for elements in generator:
    print(elements)
    counter += 1
print(counter)
