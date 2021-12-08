class MemoryClass:

    def __init__(self, list):
        self.list_of_items = list
    # ta funkcja pozwala wywolywac instancje klas tak jakby byly funkcjami

    def __call__(self, item):
        # polecenie dodajace do listy nowy parametr
        self.list_of_items.append(item)
# stworzenie instancji, ktora bedzie przechowywala pusta liste


mem = MemoryClass([])
print("List of items in memory", mem.list_of_items)
# dzieki funkcji __call__ teraz mozemy wywolywac funkcja sama nazwa zmiennej, teraz jesst callable
mem("buy milk")
print("List of items in memory", mem.list_of_items)

# klasa jest obiektem wywolywalnym
print("This class is collable ", callable(MemoryClass))
print("Callable", callable(mem))  # sama instancja nie jest callable
