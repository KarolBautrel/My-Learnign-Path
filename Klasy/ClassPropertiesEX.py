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

    texting = property(__get_text, __set_text, None)


cake_01 = Cake("Dirty Harry", "Muffin", "Sweet",
               ["Peanuts"], "Coconut", True, "")
cake_02 = Cake("Jimmy", "Cookie", "Vanila", ["Oranges"], "None", False, "")
cake_03 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True, "")


cake_01.texting = "Aliwederzi"
cake_02.texting = "Happy Birthday ! "


print("In today's offer: ")
for c in Cake.bakery_offer:
    c.show_info()
