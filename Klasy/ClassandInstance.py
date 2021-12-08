class Car:

    numberOfCars = 0
    listOfCars = []

    # kontruktor ma na celu poukladac/zainicjowac obiekt wartosciami przekazanymi w funkcji init

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk):  # atrybuty
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.IsPaintingOk = isPaintingOk
        self.isMechanicOk = isMechanicOk
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
        print("-"*20)


print('Class level variables BEFORE creating instances: ',
      Car.numberOfCars, Car.listOfCars)

car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car("Opel", "Corsa", True, False, True)  # obiekty/instancje

print("Class level AFTER creating instances: ",
      Car.numberOfCars, Car.listOfCars,)
print("\n")
print(id(Car))  # klasa istnieje, ma swoj wlasny ideyntyfikator
print("Check if obejct belong to class:", isinstance(
    car_01, Car))  # check if car_01 belongs to class Car
# other method to find if car_01 belongs to class Car
print("Check if obejct belong to class:", type(car_01) is Car)
print("Check if obejct belong to class:", car_01.__class__)
# shows all attributes of this instance as dictionary
print("List of instance attribute:", vars(car_01))
# shows methods and attributes of Class
print("List of class attribute:", vars(Car))
print("\n")
# dir shows every method you can use on this instance
print("List of instance attribute:", dir(car_01))
print('-'*30)
# dir shows every method you can use on this Class
print("List of class attribute:", dir(Car))
print("\n")

print("Value taken from instance: ", car_01.numberOfCars, Car.numberOfCars)
