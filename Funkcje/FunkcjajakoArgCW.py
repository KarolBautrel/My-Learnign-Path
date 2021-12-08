def double(x):
    return 2 * x


def square(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x/2


operations = [double, square, negative, div2]


def generate_values(transformation, x_table):
    value_list = []
    for x in x_table:
        value_list.append(transformation(x))
    return value_list


x_table = list(range(11))


print(generate_values(double, x_table))
