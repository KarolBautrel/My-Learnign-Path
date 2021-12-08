brandOnSale = 'Opel'


class Car:

    # kontruktor ma na celu poukladac/zainicjowac obiekt wartosciami przekazanymi w funkcji init

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):  # atrybuty
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        # __variable is to define that something is hide. It wont appear outside of class in any fulfill
        self.__isOnSale = isOnSale

    # we are hiding it becasue of property IsOnSale

    @property  # Nowa metoda uzywania properyu
    def isOnSale(self):
        return self.__isOnSale

    @isOnSale.setter  # setter wskazuje funkcje, dzieki ktorej zmieniamy wartosc zmiennej
    def isOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print("Changing status to {} for {} ".format(
                newIsOnSaleStatus, self.brand))
        else:
            print("Cannot change due to car is not on sale")
    # this is for setting a function that change something
    # (which method can get a value, Which can change it, which can delete it)

    @isOnSale.deleter  # deleter odpowiada za usuwanie roznych wartosci z funkcji
    def isOnSale(self):
        self.__isOnSale = None
        return "Deleted"

    @property
    def carTitle(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model).title()


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car("Opel", "Corsa", True, False, True, True)

print(car_01.isOnSale)  # dzieki property mozemy uzywac nazwy funkcji bez nawiasow
car_01.isOnSale = True
del car_01.isOnSale  # Aby usunac nalezy uzyc metody funkcji deleter
print(car_01.isOnSale)
print(car_01.carTitle)
