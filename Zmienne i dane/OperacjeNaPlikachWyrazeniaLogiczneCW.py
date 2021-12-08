import os

path = r'D:\python.txt'


def str_Counter(path):
    with open(path, 'r') as file:
        file = file.read()
        wordCount = len(file)
    return wordCount


strCount = str_Counter(path)
if os.path.isfile(path):
    print("Jest", strCount, "liter  w pliku o nazwie", path)
