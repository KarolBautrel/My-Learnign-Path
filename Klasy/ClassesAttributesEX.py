class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling


cake_01 = Cake("Dirty Harry", "Muffin", "Sweet", "Peanuts", "Coconut")
cake_02 = Cake("Jimmy", "Cookie", "Vanila", "Oranges", "None")


bakery_offer = [cake_01, cake_02]

for cakes in bakery_offer:
    print("The name is:" + cakes.name + "\n The kind is: " +
          cakes.kind+"\n The taste is: " + cakes.taste)
