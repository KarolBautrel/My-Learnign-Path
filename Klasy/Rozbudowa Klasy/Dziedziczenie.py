brandOnSale = "Opel"


class Car:
    numberofCars = 0
    listofCars = []

    # kontruktor ma na celu poukladac/zainicjowac obiekt wartosciami przekazanymi w funkcji init

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):  # konstruktor
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        self.isOnSale = isOnSale
        Car.numberofCars += 1
        Car.listofCars.append(self)

    def isDamaged(self):
        return not(self.isAirBagOk and self.IsPaintingOk and self.isMechanicOk)

    def getInfo(self):  # jesli metoda ma tylko self, to nie przyjmuje zadnych parametrow i pracuje na tym co podane w __init__
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOk))
        print("Painting - ok - {}".format(self.IsPaintingOk))
        print("Mechanic - ok - {}".format(self.isMechanicOk))
        print("IS ON SALE : {}".format(self.isOnSale))

    def __getIsOnSale(self):  # we are hiding it becasue of property IsOnSale
        return self.__isOnSale

    # we are hiding it becasue of property IsOnSale
    def __setIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print("Changing status to {} for {} ".format(
                newIsOnSaleStatus, self.brand))
        else:
            print("Cannot change due to car is not on sale")

    IsOnSale = property(__getIsOnSale, __setIsOnSale, None)


# klasa ciezarowki, ktora dziedziczy z auta, jest dzieckiem.
class Truck(Car):
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale, capacityKG):
        # Funkcja super powoduje, ze wszsytkie atrybuty w nawiasie beda dziedziczone z klasy - rodzica
        super().__init__(brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale)
        # dodanie atrybutu nowego, niedziedziczonego.
        self.capacityKG = capacityKG
# dziedzioczona metoda getInfo aby dodac nowe mozliwosci do metody, ktora juz istenieje to wystarczy ja dopisac
# i dodac potem super().metodazKlasyRodzica()

    def getInfo(self):
        super().getInfo()  # metoda z Rodzica (getInfo z klasy Car)
        # Dopisana nowa czesc do tej metody juz dla klasy Truck
        print("Capacity in Kgs: {}".format(self.capacityKG))


car_01 = Car('Seat', 'Ibiza', True, True, True, True)
car_02 = Car("Opel", "Corsa", True, False, True, [])  # obiekty/instancje

truck_01 = Truck("Ford", "Transit", True, True, True,
                 False, 1600)  # obiekty klasy Truck
truck_02 = Truck("Renault", "Trafic", True, True, True, True, 1200)
# += poniewaz funkcja iadd to wlasnie odzwierciedlenie +=

print(truck_01.brand, truck_01.capacityKG)
truck_01.getInfo()
