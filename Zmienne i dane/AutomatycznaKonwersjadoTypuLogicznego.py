listofError = [101, 102, 103]
print("Variable is ok", listofError, type(listofError))
# instrukcja nie wykona sie gdy napis jest pusty. samo if [zmienna] sprawdza czy on po prostu istnieje
# Pamietac, ze liczba powyzej/ponizej zera da true, a 0 da false
if len(listofError) > 0:  # jezeli ilosc elementwo jest wieksza od 0
    print('TRUE')
