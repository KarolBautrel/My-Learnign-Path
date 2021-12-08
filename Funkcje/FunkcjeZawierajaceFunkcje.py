def Calculate(kind='+', *args):
    result = 0
    if kind == '+':
        for a in args:
            result += a
    elif kind == '-':
        for a in args:
            result -= a
    return result


print(Calculate('+', 1, 2, 3))
print(Calculate('-', 1, 2, 3))

# funkcja odpowiadajaca za dodawnaie/odejmowanie


def create_function(kind='+'):
    source = '''
def f(*args):
    result = 0
    for a in args:
        result{}=a
    return result 
'''.format(kind)
    exec(source, globals(
    ))  # exec wykonuje cala sekwencje podana w zmiennej source (nalezy uzyc .globals)
    return source  # TU MA BYC F


f_add = create_function('+')  # zapamietanie funkcji w zmiennej
print(f_add(1, 2, 3, 4, 5))
f_subs = create_function('-')
print(f_subs(10, 20, 30, 40))
