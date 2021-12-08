import os

path = r'D:\python.txt'

# os.remove(path)  # usuniecie pliku przypisanego do sciezki w zmiennej path

# czy znajduje sie plik w danej sciezce
# pomimo braku plikue, przez "or" program wykonuje dodana operacje, wiec zamiast wyswietlic false, tworzy plik i zwaraca none
result = os.path.isfile(path) or open(path, 'x').close()
# or = alternatywa  and = koniunkcja
print(result)


def CountWords(path):
    with open(path, 'r', encoding='utf-16') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count


path = r'c:\temp\test.txt'
if os.path.isfile(path):
    print("There are {} words in the file {}".format(CountWords(path), path))


os.path.isfile(path) and print(
    "There are {} words in the file {}".format(CountWords(path), path))
