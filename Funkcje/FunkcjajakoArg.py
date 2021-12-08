def Bake(what):
    print("Baking {}".format(what))


def Add(what):
    print("Adding {}".format(what))


def Mix(what):
    print("Mixing {}".format(what))


cookbook = [(Add, 'milk'), (Add, 'eggs'), (Add, 'sugar'),
            (Mix, 'ingredients'), (Bake, 'cookies')]

for activity, obj in cookbook:  # dla elementow tupletow
    activity(obj)  # element 1 funkcja (2element zmienna)

print('-'*30)


def Cook(activity, obj):  # funkcja przyjmuje argument activity i objec
    activity(obj)  # wykonuje activity na obj


# funkcja bake wykonuje activities na obiekcie brownies
Cook(Bake, 'brownies')  # activity - funkcja Bake obj = 'brownies'.

for activity, obj in cookbook:
    Cook(activity, obj)
