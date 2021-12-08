import datetime
# Assert to zalozenie, ze jakis warunek jest spelniony


netto = 100
brutto = 120


assert netto <= brutto, "Netto cant be greater than brutto"


orderDate = datetime.date(2022, 10, 13)
deliveryDate = datetime.date(2022, 10, 11)

# assert pozwala blyskawicznie przetestowac czy dany blad wystepuja i mozna dopisac komentarz
assert orderDate <= deliveryDate, "Order date cannot be later than deliver"
