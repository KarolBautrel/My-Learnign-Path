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

    def __exit__(self, exc_type, exc_value, trace):
        pass


# przekazuje sciezke dostepu do pliu (self.path)
ini = Ini_file(
    r"D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager\my.ini")
ini.write_parameter('version', 1)  # dodaje do slownika parametrty
ini.write_parameter('level', 'advanced')  # dodaje do slownika parametrty
ini.save_on_disk()  # zapisuje na dysku


with Ini_file(
        r"D:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Context Manager\my.ini") as ini2:
    print((ini2.parameters))
    print(ini2.read_parameter('version'))
    print(ini2.read_parameter('level'))
