class Cake:

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-'*20)

    def __str__(self):
        return "Name: {}, Kind: {}, additives: {}".format(self.name, self.kind, self.additives)

    def __iadd__(self, other):
        additives = self.additives
        if type(other) is list:
            additives.extend(other)
            return self
        elif type(other) is str:
            additives.append(other)
            return self
        else:
            raise Exception("Wrong type: {}".format(type(other)))


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla',
              ['chocolade', 'nuts'], 'cream')


cake01 += ["Vanilla", "Bananas"]
cake01 += "Apples"
cake01.show_info()
