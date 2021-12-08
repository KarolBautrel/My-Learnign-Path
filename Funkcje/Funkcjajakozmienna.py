def GoLeft(*args):
    print('PLACEHOLDER - turning left with', *args)


def GoRight(*args):
    print('PLACEHOLDER - turning right with', *args)


def GoForward(*args):
    print('PLACEHOLDER - going forward with', *args)


def GoBack(*args):
    print('PLACEHOLDER - going back with', *args)


def Start(*args):
    print('PLACEHOLDER - starting with', *args)


def Stop(*args):
    print('PLACEHOLDER -stopping with', *args)


instructions = [Start, GoForward, GoForward, GoLeft,
                GoForward, GoRight, Stop]  # lista funkcji, ruchy robota

dish = "spaghetti"

for instr in instructions:  # dla kazdej instrukcji w instukcje
    instr(dish)  # argument funkcji (Dish)
