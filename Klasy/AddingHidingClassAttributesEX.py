class Cake:

    known_types = ['Cookie', 'Muffin', 'meringue', 'biscuit',
                   'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.__gluten_free = gluten_free
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
        print('-'*40)

    def set_filling(self, filling):
        self.filling = filling

    def set_additives(self, additives):
        self.additives = additives


cake_01 = Cake("Dirty Harry", "Muffin", "Sweet", ["Peanuts"], "Coconut", True)
cake_02 = Cake("Jimmy", "Cookie", "Vanila", ["Oranges"], "None", False)
cake_03 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', True)


print("In today's offer: ")
for c in Cake.bakery_offer:
    c.show_info()
