# grep to polecenie, ktore ma za zadanie znalezc w systemie operacyjnym plikow, ktore zawieraja konkretny ciag znakow


import os


path = r"E:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Klasy"
search_string = "Ford"
file_extensionGlobal = ".py"
# walk() generates the file names in a directory tree by walking the tree either top-down or bottom-up.
for dir_name, subdirs, filenames in os.walk(path):
    # nazwa katalogu, nazwy wszystkich podkatalogow, nazwy plikow
    #print(dir_name, subdirs, filenames)
    for filename in filenames:  # dla plikow w liscie plikow
        if filename.endswith(file_extensionGlobal):  # jesli plik konczy sie na ".py"
            # wyznacz sciezke do tego pliku
            fullFileName = os.path.join(dir_name, filename)
            # dla kazdej lini w otwartym pliku z powyzszej sciezki
            for line in open(fullFileName):
                if search_string in line:  # jesli w lini jest search_strin
                    print(filename)  # Wyswietl nazwe pliku


# STWORZENIE GENERATORA ZWRACAJACEGO NAZWY PLIKOW
def generate_file(base_dir, file_extension):
    for dir_name, subdirs, filenames in os.walk(base_dir):
        # nazwa katalogu, nazwy wszystkich podkatalogow, nazwy plikow
        for filename in filenames:  # dla plikow w liscie plikow
            if filename.endswith(file_extension):  # jesli plik konczy sie na ".py"
                # wyznacz sciezke do tego pliku
                fullFileName = os.path.join(dir_name, filename)
                yield fullFileName

# STWORZENIE GENERATORA DO WYSZUKIWANIA CIAGOW ZNAKOW W LISTACH PLIKOW WCZESNIEJ WYGENEROWANYCH
# search_string = wyszukiwany tekst, files = kolekcja plikow, ktora ma byc przeszukiwana


def grep_file(search_string, files):
    for file in files:
        with open(file) as text:
            if search_string in text.read():  # read bo otwieramy plik
                yield file


# przypisujemy do zmiennej wyniki funkcji generujacej nazwy plikow
files_generetaror = generate_file(path, file_extensionGlobal)

# search string = szukana fraza, files_generator = listaw wygenerowanych wczesniej plikow
for file in grep_file(search_string, files_generetaror):
    print(file)
