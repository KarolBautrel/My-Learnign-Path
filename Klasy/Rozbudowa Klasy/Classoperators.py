class Car:
    # kontruktor ma na celu poukladac/zainicjowac obiekt wartosciami przekazanymi w funkcji init
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, accesories):  # konstruktor
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.accesories = accesories

    def getInfo(self):  # jesli metoda ma tylko self, to nie przyjmuje zadnych parametrow i pracuje na tym co podane w __init__
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOk))
        print("Painting - ok - {}".format(self.IsPaintingOk))
        print("Mechanic - ok - {}".format(self.isMechanicOk))
        print("Accesories: {}".format(self.accesories))
        print("-"*20)

    # funkcja dunder "iadd" to funkcja, ktora odpowiada za +=
    def __iadd__(self, other):
        accesories = self.accesories
        if type(other) is list:  # jesli other to lista
            accesories.extend(other)
            # stworzoona zostanie nowa instancja ze zmieniony atrybutem accesories
            return self
        elif type(other) is str:  # jezeli other to str
            accesories.append(other)
            return self
        else:
            # jesli podamy atrybut w innej formie niz lista, string
            raise Exception("Car {} is not implemented".format(type(other)))

    # funkcja add to funkcja +
    def __add__(self, other):
        if type(other) is Car:
            return [self, other]
        else:
            raise Exception("Type : {} is not implemented".format(type(other)))
    # sluzy do wyswietlania jakiejs zawartosci po wywolaniu tylko instancji.

    def __str__(self):
        return ("Brand: {}, Model: {}".format(self.brand, self.model))


car_01 = Car('Seat', 'Ibiza', True, True, True, ["winter tires "])
car_02 = Car("Opel", "Corsa", True, False, True, [])  # obiekty/instancje
# += poniewaz funkcja iadd to wlasnie odzwierciedlenie +=
car_01 += ["navigatton", "roof rack"]


carList = car_01 + car_02
print(carList[0].brand, carList[1].brand)

for i in carList:
    print(i.getInfo())

print(car_01)
