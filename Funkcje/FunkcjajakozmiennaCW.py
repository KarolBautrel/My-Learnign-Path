def double(x):
    return 2 * x


def square(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x/2


number = 8

transformations = [double, square, negative, div2]
tmp_return_value = number
transformations2 = [square, square, div2, double]

for trans in transformations2:
    tmp_return_value = trans(tmp_return_value)
    print(tmp_return_value)
