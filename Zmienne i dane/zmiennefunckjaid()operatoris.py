myvar = 'Hello Pycharm'
myvar2 = myvar + "!!"
print(myvar, myvar2)

print(type(myvar), type(myvar2))
print('Is value the same ?', myvar == myvar2)
print('Are the variables the same?', myvar is myvar2)
# adresy sa takie same, poniewaz przechowuja ta sama wartosc
print(id(myvar), id(myvar2))
myvar2 = myvar2[:-2]
print()
print(type(myvar), type(myvar2))
# porownanie wartosci == sprawdza czy wartosci sa takie same
print('Is value the same ?', myvar == myvar2)
# porownanie czy zmienne maja ten sam adres w pamieci komputera
print('Are the variables the same?', myvar is myvar2)
# adresy sa takie same, poniewaz przechowuja ta sama wartosc
print(id(myvar), id(myvar2))
