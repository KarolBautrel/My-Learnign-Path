import os


class Ini_file:

    def __init__(self, path):
        self.path = path
        self.parameters = {}  # Slownik, ktory bedzie przechowywal dane znajdujace sie w pliku
        self.read_from_disk()  # metoda odpowiadajaca za odczyt danych z pliku

    def read_from_disk(self):
        # sprawdza czy plik wskazany w metodzie init jest plikiem
        if os.path.isfile(self.path):
            with open(self.path) as f:
                for line in f:
                    # dzielimy linie ze wzgledu na znak rownosci
                    parts = line.replace('\n', '').split('=')
                    # funkcja zapisujaca wartosci do slownika
                    self.parameters[parts[0]] = parts[1]

    def read_parameter(self, key):  # argument key
        if key in self.parameters.keys():  # czy klucz podany jako argument znajduje sie w liscie kluczy w slowniku self.parameters
            return self.parameters[key]  # zwaraca wartosc tego klucza

    # umieszczenie pod klucz key wartosc value w argumencie

    def write_parameter(self, key, value):
        self.parameters[key] = value

    def save_on_disk(self):
        with open(self.path, 'w') as file:
            for key, value in self.parameters.items():  # Pobranie wartosci ze slownika
                # zzapisanie ich do zmiennej w odpowiednije formie
                line = "{}={}\n". format(key, value)
                # zapisanie ich we wczesniej otwartym pliku
                file.writelines(line)

    def __enter__(self):
        return self
    # exc_type = rodzaj bledu, exc_value = wartosc bledu(komunikat), trace = powiazanie bledu z mozliwymi wczensiejszymi bledami tej instrukcji

    def __exit__(self, exc_type, exc_value, trace):
        print("__exit__")
        # wypisanie wartosci bledy, rodzaju oraz mozliwych powiazan
        print('exc_type={}'.format(exc_type))
        print('exc_value={}'.format(exc_value))
        print('exc_trace ={}'.format(trace))
        # wywolanie bledu na zewnatrz jesli to bedzie OSError
        if exc_type == OSError:
            return False
        # w przypadku innego bledu ukrywamy go i context manager pracuje dalej
        else:
            return True


# jesli w bloku with dojdzie do bledu, to context manager wysle do metody exit informacje na temat tego bledu(exc_type,exc_val,trace)
# metoda exit wtedy moze zdecydowac co z bledem zrobic
with Ini_file(
        r"D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager\my.ini") as myini:
    myini.write_parameter('mode', 'strict')  # dodaje do slownika parametrty
    # dodaje do slownika parametrty('loglevel')
    myini.write_parameter('loglevel', 'light')
    myini.save_on_disk()
    print(10/0)
