import pickle
import glob


class Cake:

    known_types = ['Cookie', 'Muffin', 'meringue', 'biscuit',
                   'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__gluten_free = gluten_free
        if self.kind == "Cookie" or text == '':
            self.__text = text
        else:
            self.__text = ""
            print("Text can be set only for Cookie")
        Cake.bakery_offer.append(self)

    def show_info(self):
        print("Name: {}".format(self.name))
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives: ")
            for i in self.additives:
                print("\t{}".format(i))
        print("Filling: {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text : {}".format(self.__text))
        print('-'*40)

    def set_filling(self, filling):
        self.filling = filling

    def set_additives(self, additives):
        self.additives = additives

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == "Cookie":
            self.__text = new_text
            print("Changing text to {}".format(new_text))
        else:
            print("Text is only allowed for Cookies")

    def save_to_file(self, path):
        with open(path, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as file:  # odczytanie pliku w trybie binarnym
            # Wczytanie pliku i zapisanie jego wartosci w zmienniej new_file
            new_file = pickle.load(file)
        # Dodanie nowego pliku do listy klasowej cls.bakery_offer
        cls.bakery_offer.append(new_file)
        return new_file
    texting = property(__get_text, __set_text, None)

    @staticmethod
    def get_bakery_files(name):
        # zwraca wszystkie pliki ze sciezki o rozszerzeniu *bakery
        return glob.glob(name+"/*bakery")


cake_01 = Cake("Dirty Harry", "Muffin", "Sweet",
               ["Peanuts"], "Coconut", True, "")
cake_02 = Cake("Jimmy", "Cookie", "Vanila", ["Oranges"], "None", False, "")
cake_03 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, "")


cake_01.texting = "Aliwederzi"
cake_02.texting = "Happy Birthday ! "


cake_01.save_to_file("cake01.bakery")
cake_02.save_to_file("cake02.bakery")


cake_04 = Cake.read_from_file("cake01.bakery")

# print(Cake.bakery_offer)

print(Cake.get_bakery_files("d:/Python/Python/Kody nauka"))
