import csv
import types  # biblioteka sluzaca do m.in przypisywania funkcji do funkcji klasowej

# sciezka,lista naglowkow, lista wartosci w pliku

# Funkcja statyczna przyjmuje kilka parametrow i za kazdym razem je trzeba przekazac


def exportToFile_Static(path, header, data):
    with open(path, "w") as file:
        # Tworzymy obiekt writer, deklaruje jak pracowac z plikiem csv, delimeter = oznacza czym oddzielamy slowa.
        # jezeli w wartosciach tekstowych beda przecinki to zamykamy w cudzyslowie (quotechar)
        # quoting okresla jak mocno cytowane maja byc wszystkie wartosci(minimal oznacza, ze w cudzyslowiu beda te wartosci, ktore w srodku zawieraja przecinek)
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # writerow odpowiada za zapisanie w pliku wartosci z argumentu "Header"
        writer.writerow(header)
        # writerow odpowiada za zapisanie w pliku wartosci z argumentu "data"
        writer.writerow(data)
    print(">>>This is function exportToFile - static method")


# Funkcja na poziomie klasy jako pierwszy argument przyjmuje klase(cls), ale zrobi to za Ciebie python za pomoca types.methodtype
def exportToFile_Class(cls, path):
    with open(path, "w") as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Tym razem z poziomu klasy nie musimy podawac co ma byc zapisane, bo jest juz to w funkcji
        writer.writerow(['brand', 'model', 'IsOnSale'])
        # Uzywamy pętli, aby dla kazdego elementu w liscie "list of cars" z klasy wypisac wartosci zmiennych brand,model,isOnSale
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print(">>>This is function exportToFile - class method")


# Funkcja na poziomie Instancji jako pierwszy argument przyjmuje self i rowniez uzywamy types.methodtype
def exportToFile_Instance(self, path):
    with open(path, "w") as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Tym razem z poziomu klasy nie musimy podawac co ma byc zapisane, bo jest juz to w funkcji
        writer.writerow(['brand', 'model', 'IsOnSale'])
        # uzywamy parametrow danej isntancji (self.)
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print(">>>This is function exportToFile - instance method")


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


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car("Opel", "Corsa", True, False, True, True)
print("Static ------------" * 9)
# przypisanie funkcji poza klasa do funkcji w klasie za pomoca dopisania nazwy klasy przed funkcja
Car.ExportToFile_Static = exportToFile_Static
# exportToFile_Static("export_static.csv", ["Brand", "Model", "IsOnSale"], [
# car_01.brand, car_01.model, car_01.IsOnSale])  # (path,header,data)
# wywolanie funkcji z poziomu klasy
Car.ExportToFile_Static("export_static.csv", ["Brand", "Model", "IsOnSale"], [
    car_01.brand, car_01.model, car_01.IsOnSale])
print("Static ------------" * 9)
# metoda ktora przybindowuje funkcje (pierwszy argument) do danej klasy(drugi arg)
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class("export_class.csv")

print("Static ------------" * 9)
# metoda ktora przybindowuje funkcje (pierwszy argument) do danej instancji(drugi arg)
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(path="export_instance.csv")

print("-"*40)
# Sprawdzenie czy metoda istnieje na poziomie, statycznyn,klasy i instancji. Wybieramy obiekt, bo jesli klasa ma metode to obiekt tez
# hasattr = czy istnieje atrybut o nazwie funkcji dla danego obiektu, poniewaz metoda obiektu jest tez jego atrybutem
# callable = sprawdzenie, czy nazwe da sie uruchomic jako funkcje
if hasattr(car_01, 'ExportToFile_Static') and callable(car_01.ExportToFile_Static):
    print("The object has method ExportToFile_Static")
if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print("The object has method ExportToFile_Class")
if hasattr(car_01, 'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print("The object has method ExportToFile_Instance")
if hasattr(car_01, 'IsOnSale') and callable(car_01.IsOnSale):  # property nie jest callable
    print("The object has method ExportToFile_Instance")
else:
    print("No such method")
