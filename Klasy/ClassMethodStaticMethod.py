brandOnSale = 'Opel'


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

    def isDamaged(self):
        return not (self.isAirBagOk and self.IsPaintingOk and self.isMechanicOk)

    def getInfo(self):  # jesli metoda ma tylko self, to nie przyjmuje zadnych parametrow i pracuje na tym co podane w __init__
        # if method has only self in arguments so its working only on parameteres set in __init__
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag - ok - {}".format(self.isAirBagOk))
        print("Painting - ok - {}".format(self.IsPaintingOk))
        print("Mechanic - ok - {}".format(self.isMechanicOk))
        print('IS ON SALE: {}'.format(self.__isOnSale))
        print("-"*20)

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
    # this is for setting a function that change something
    # (which method can get a value, Which can change it, which can delete it)
    IsOnSale = property(__getIsOnSale, __setIsOnSale, None)

    @classmethod  # decorator which show this is class method.
    def readFromText(cls, aText):  # cls means class its shorcut
        aNewCar = cls(*aText.split(':'))  # * is for sending elements for list.
        return aNewCar

    @staticmethod  # decorator which show this is static method
    # static method does not need to self argument, because its not working on instance. This method is independent
    def convert_KMtoKW(KM):
        return KM * 0.735

    @staticmethod
    def convert_KWtoKM(KW):
        return KW * 1.36


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car("Opel", "Corsa", True, False, True, True)


lineOfText = 'Renault:Megane:True:True:False:False'
# method which allows you to read from string attributes for new instance
car_03 = Car.readFromText(lineOfText)

print("Converting 120 KM to KW", Car.convert_KMtoKW(120))
print("Converting 120 KW to KM", Car.convert_KWtoKM(120))
