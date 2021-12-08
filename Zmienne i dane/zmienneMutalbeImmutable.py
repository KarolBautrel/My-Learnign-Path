number = 10
print("Var number", number, id(number))
number += 2  # Po zmianie wartosci zmiennej dostaje ona inne miejsce, ma inne Id
print("Variable number", number, id(number))  # zmienne pokazuja inne Id
text = "africa"
print("variable text", text, id(text))
text += "is hot"  # Po zmianie wartosci zmiennej dostaje ona inne miejsce, ma inne Id
# zmienne pokazuja inne iD jest immutable
print("variable text", text, id(text))

list = [1, 2, 3]
print("variable list", list, id(list))
# Wartosc sie nie zmienia, poniewaz miejsce listy sie nie zmienia
list.append(4)
# Mmutable, Id sie nie zmienilo, mozna zmieniac
print("variable list", list, id(list))
print()
list2 = list  # teraz list2 i list wskazuja na ten sam obszar pamieci
print("variable list", list2, id(list2))
list2.append(5)  # dodalismy 5 do listy 2
print("variable list", list, id(list))  # wartosc zostala dodana do obu list
print("variable list", list2, id(list2))
print()
# funkcja copy sprawia, ze list3 ma takie same wartosci jak list, ale
# juz jest skierowana w inna komorke pamieci
list3 = list.copy()
print("variable list", list, id(list))  # listy maja inne Id
print("variable list", list3, id(list3))
list3.append(6)  # wartosc 6 zostala dodana tylko do list3
print("variable list", list, id(list))
print("variable list", list3, id(list3))
