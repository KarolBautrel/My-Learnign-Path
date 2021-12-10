import itertools as it


myList = ['a', 'b', 'c', 'd']
# combinations z itertools sluzy do budowania kombinacji, kolejnosc sie NIE LICZY
combination = it.combinations(myList, 3)

# permutacje robia z powtorzeniami kolejnosc sie LICZY
permutations = it.permutations(myList, 3)

products = it.product(myList, repeat=3)


# kombinacje ze zwracaniem
combination_with_replacement = it.combinations_with_replacement(myList, 3)

# Na ile sposob mozna z zawartosci portfela ponizej zaplacic 100 zlotych
wallet = [20, 20, 20, 20, 10, 10, 10, 5, 5, 1, 1, 1]
result = []
for i in range(0, 101):  # dla i w zasiegu 0 do 101 (bo 100 zlotych)
    # dla kombinacji (iterable element, w zasiegu i)
    for combination in it.combinations(wallet, i):
        if sum(combination) == 100:  # jesli combination sumuje sie do stu
            result.append(combination)  # dodaj do listy


result = set(result)  # zamiana na set zeby uniknac powtorek
for i in result:
    print(i)


print("\n")
money = [50, 20, 10]

for i in range(1, 101):
    for combination in it.combinations_with_replacement(money, i):
        if sum(combination) == 100:
            print(combination)
