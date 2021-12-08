class Car:

    numberOfCars = 0
    listOfCars = []

    # kontruktor ma na celu poukladac/zainicjowac obiekt wartosciami przekazanymi w funkcji init

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale):  # atrybuty
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
        # __variable is to define that something is hide. It wont appear outside of class in any fulfill
        self.__isOnSale = isOnSale
        # when we create new car instance numberOfCars variable will get bigger by 1
        Car.numberOfCars += 1
        # when we create new car instance we will append it to listOfCars
        Car.listOfCars.append(self)

    def isDamaged(self):  # return False if. IsDamaged = False(no)
        return not (self.isAirBagOk and self.IsPaintingOk and self.isMechanicOk)

    def getInfo(self):  # jesli metoda ma tylko self, to nie przyjmuje zadnych parametrow i pracuje na tym co podane w __init__
        # if method has only self in arguments so its working only on parameteres set in __init__
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOk))
        print("Painting - ok - {}".format(self.IsPaintingOk))
        print("Mechanic - ok - {}".format(self.isMechanicOk))
        print('IS ON SALE: {}'.format(self.__isOnSale))
        print("-"*20)


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car("Opel", "Corsa", True, False, True, True)

car_02.__isOnSale = False  # it wont appear in function.
car_02.YearOfProduction = 2005  # making a new attribute to instance
del car_02.YearOfProduction  # deleting attribute from instance
# Adding attribute function (instance, nameofattribue, value)
setattr(car_02, 'TAXI', False)
delattr(car_02, 'TAXI')  # deleting specific attribute from instance
# method which check if instance has specific attribute
print(hasattr(car_02, 'TAXI'))

print(vars(car_02))
