import random


class MemoryClass:

    list_of_already_selected_items = []

    # argumentem przekazywanym do init jest nazwa funkcji
    def __init__(self, funct):
        print("This is init of MemoryClass")
        # nazwa funkcji zapamietana zostanie w wewnetrznej instancyjne funct
        self.funct = funct

    def __call__(self, list):
        print("THIS IS CALL OF MEMORYCLASS INSTANCE")
        # Dodaj do listy kazdy przedmiot z listy jesli nie znajduje sie on w liscie z MemoryKlass list_of_already_selected_items
        items_not_selected = [
            i for i in list if i not in MemoryClass.list_of_already_selected_items]
        print("+--selecting only from a list of", items_not_selected)
        # w zmiennej item zostanie zapisana wartosc wykonanej funkcji(zostanie wylosowany jeden element)
        item = self.funct(items_not_selected)
        # element ten zostanie od razu dodany do listy z juz wybranymi elementami
        MemoryClass.list_of_already_selected_items.append(item)
        return item


cars = ['Opel', 'Toyota', 'Fiat', 'Ford', 'Renault', 'Mercedes',
        'BMW', 'Peugeot', 'Porsche', 'Audi', 'VW', 'Mazda']


@MemoryClass  # dekorator pokazujacy ze funkcje ta uzywamu z klasa MemoryClass
# nalezy pamietac aby dodac funkcje __call__, aby instancja byla callable
def selectTodayPromotion(list_of_cars):
    return random.choice(list_of_cars)


@MemoryClass
def selectTodayShow(list_of_cars):
    return random.choice(list_of_cars)


@MemoryClass
def selectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)


print("Promotion: ", selectTodayPromotion(cars))
print("Show: ", selectTodayShow(cars))
print("Free accessories: ", selectFreeAccessories(cars))
