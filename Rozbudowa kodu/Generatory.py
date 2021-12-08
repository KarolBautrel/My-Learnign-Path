listA = list(range(6))
listB = list(range(6))


product = []

for a in listA:
    for b in listB:
        product.append((a, b))

product = [(a, b) for a in listA for b in listB if a % 2 == 1 and b %
           2 == 0]  # przeiteruj dodaj a,b jest a nieparzyste i b parzyste


product = {a: b for a in listA for b in listB if a % 2 == 1 and b %
           2 == 0}  # tylko klucze zostana przefiltorwane, poniewaz wartosci nadpisuja sie przy takich samych kluczach

gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b %
       2 == 0)  # generator rozni sie tym od petli zagniezdzonej tym, ze uzywamy nawiasow okraglych. Generator dobry bedzie jesli potrzeba przetwarzac ogromna ilosc danych bez zapisywania

print(next(gen))  # first elem
print(next(gen))  # sec elem
print(next(gen))  # third elem
print()
for elem in gen:  # porgram zapamietuje gdzie skoczylismy i kontynuuje od tego punktu
    print(elem)

gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b %
       2 == 0)
print()
while True:
    try:
        print(next(gen))
    except StopIteration:
        print("All values have been generater")
        break
