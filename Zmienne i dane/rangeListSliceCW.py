import itertools

colorList = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']


def new_color_list(list, n):
    n = list[:n].copy()
    return n


for items in range(0, len(colorList)+1):
    for subset in itertools.combinations(colorList, items):
        print(subset)

for i in range(1, len(colorList)+1):
    print(new_color_list(colorList, i))


string = ('''Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką
 prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym 
 miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. 
 Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.''')

print(string.replace(
    "(z łac. corpo – ciało, ratus – szczur; pol. ciało szczura)", ''))
