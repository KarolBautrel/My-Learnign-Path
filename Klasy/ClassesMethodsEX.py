class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling

    def show_info(self):
        print("Name: {}".format(self.name))
        print("Kind: {}".format(self.kind))
        print("Taste: {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives: ")
            for i in self.additives:
                print("\t{}".format(i))
        print("Filling: {}".format(self.filling))
        print('-'*40)

    def set_filling(self, filling):
        self.filling = filling

    def set_additives(self, additives):
        self.additives = additives


cake_01 = Cake("Dirty Harry", "Muffin", "Sweet", "Peanuts", "Coconut")
cake_02 = Cake("Jimmy", "Cookie", "Vanila", [
               "Oranges", "Chocolade"], "Strawberry")


cake_01.set_filling("Cranberry")

cake_01.set_additives(["peanuts", "cornflakes"])

bakers_offer = [cake_01, cake_02]


print("In today's offer: ")
for c in bakers_offer:
    c.show_info()
