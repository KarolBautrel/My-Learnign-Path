class Car:
    # kontruktor ma na celu poukladac/zainicjowac obiekt wartosciami przekazanymi w funkcji init
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):  # konstruktor
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk

    def isDamaged(self):  # return False if. IsDamaged = False(no)
        return not (self.isAirBagOk and self.IsPaintingOk and self.isMechanicOk)

    def getInfo(self):  # jesli metoda ma tylko self, to nie przyjmuje zadnych parametrow i pracuje na tym co podane w __init__
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOk))
        print("Painting - ok - {}".format(self.IsPaintingOk))
        print("Mechanic - ok - {}".format(self.isMechanicOk))
        print("-"*20)


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car("Opel", "Corsa", True, False, True)  # obiekty/instancje


print(car_01.brand, car_01.model, car_01.isAirBagOk,
      car_01.IsPaintingOk, car_01.isMechanicOk)

print(car_02.brand, car_02.model, car_02.isAirBagOk,
      car_02.IsPaintingOk, car_02.isMechanicOk)


print(car_01.brand, car_01.getInfo())
print(car_02.brand, car_02.getInfo())
