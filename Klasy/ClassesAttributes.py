class Car:
    # kontruktor ma na celu poukladac/zainicjowac obiekt wartosciami przekazanymi w funkcji init
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):  # konstruktor
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car("Opel", "Corsa", True, False, True)  # obiekty/instancje


print(car_01.brand, car_01.model, car_01.isAirBagOk,
      car_01.IsPaintingOk, car_01.isMechanicOk)

print(car_02.brand, car_02.model, car_02.isAirBagOk,
      car_02.IsPaintingOk, car_02.isMechanicOk)
