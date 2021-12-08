cake01 = {
    'taste': 'vanilia',
    'glaze': 'chocolade',
    'text': 'Happy Brithday',
    'weight': 0.7}

cake02 = {
    'taste': 'tee',
    'glaze': 'lemon',
    'text': 'Happy Coding',
    'weight': 0.7}


def show_cake_info(aCake):
    return (aCake['taste'], aCake['glaze'], aCake['text'], aCake['weight'])


cakes = [cake01, cake02]

for c in cakes:
    print(show_cake_info(c))
