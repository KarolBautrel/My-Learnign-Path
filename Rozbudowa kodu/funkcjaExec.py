var_x = 10
password = "My super secret password"

source = '''
new_var = 1
for i in range(var_x):
    print('-'*i) 
    new_var +=i
'''

# Exec nie zwraca wartosci, zwaraca None, ale wykonuje polecenie. np przypisuje zmienna
result = exec(source)
# Exec potrafi przyjac instrukcje z wieksza ilosca linijek
print(result)

print(var_x)
# print(new_var)  # Za pomoca exec i zmiennej source stworzylismy nowa zmienna. Wyswietla blad poniewaz dopiero po stworzeniu source bedzie stworzona ta zmienna
