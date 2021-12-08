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
