class Car:
    numberofCars = 0
    listofCars = []

    # kontruktor ma na celu poukladac/zainicjowac obiekt wartosciami przekazanymi w funkcji init

    def __init__(self, brand, model, isOnSale):  # konstruktor
        print(">>>Class Car - init - Starting")
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = "Brand: {}, Model: {}".format(self.brand, self.model)
        print(">>> Class car init finishing<<<")

    def isDamaged(self):
        return not(self.isAirBagOk and self.IsPaintingOk and self.isMechanicOk)

    def getInfo(self):
        print(">>>Class Car - Get info  - Starting")
        # super().getInfo()
        print("{} {}".format(self.brand, self.model).upper())
        print("IS ON SALE : {}".format(self.isOnSale))
        print(">>>Class Car - Get info  - Finishing")


# klasa opisujaca specjalistow sprzedazy danej marki
class Specialist:
    def __init__(self, firstname, lastname, brand):
        print(">>>Class Specialist - init - Starting")
        self.firstname = firstname
        self.lastname = lastname
        self.name = "{} {}".format(self.firstname, self.lastname)
        self.brand = brand
        print(">>>Class Specialist - init - Finishing")

    def getInfo(self):
        print(">>>Class Specialist - Get info  - Starting")
        print("{} {} - ({})".format(self.firstname, self.lastname, self.brand))
        print(">>>Class Specialist - Get info  - Finishing")


# Klasa ktora dziedzicy od Car i od Specialist
class CarSpecialist(Car, Specialist):

    # funkcja konstruktor musi przyjmowac wszystkie atrybuty klas z ktorych dziedziczy.
    def __init__(self, brand, model, isOnSale, firstname, lastname):
        print(">>>Class CarSpecialist - init - Starting")
        # atrybuty dziedziczone z klasy Car
        Car.__init__(self, brand, model, isOnSale)
        # atrybuty dziedziczone z klasy Specialist
        Specialist.__init__(self, firstname, lastname, brand.upper())
        print(">>>Class CarSpecialist - init - Finishing")

    def getInfo(self):
        print(">>>CarSpecialist Method Get Info -- Starting<<<")
        # gdy podamy super().metoda przy wiekszej ilosci rodzicow
        # to wtedy funkcja ktora dziedzica wykonuje ta metoda od ostatniej do pierwszej jesli w funkcji rodzica jest metoda super()
        # jesli nie ma metody super() w funkcji rodczia to klasa dziecka zakonczy metode po znalezieniu pierwszej klasy
        # rodzica posiadajaca owa metode
        print(super().getInfo())
        print(">>>CarSpecialist Method Get Info -- finishing<<<")


tom = CarSpecialist("Toyota", "Corolla", True, "Tom", "Smith")


tom.getInfo()
# method resolution order - kolejnosc wywolywania funkcji
print(CarSpecialist.__mro__)
