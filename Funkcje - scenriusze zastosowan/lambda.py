
x = 10
# f=lambda x: x*2


def f(x, y): return x**y  # f = lambda x,y: x**y


list_numbers = [1, 2, 3, 4, 11, 14, 15, 20, 21]


def is_odd(x):
    return x % 2 != 0


# funkcja filter (funkcja, iterowany obiekt) funkcja zwraca i zapisuje elementry z warunku funkcji
filtered_list = list(filter(is_odd, list_numbers))

print(filtered_list)
# zamiast zapisywania funkcji mozemy dac funkcje lambda.
# lambda zmienna: cialo funkcji ,
filtered_list_withLambda = list(filter(lambda x: x % 2 != 0, list_numbers))
print(filtered_list_withLambda)


print(list(filter(lambda x: x % 2 != 0, list_numbers)))


def generate_multiply_functions(n):
    return lambda x: n * x  # x podawane bedzie przy wywolywaniu funkcji


mul_2 = generate_multiply_functions(2)
mul_3 = generate_multiply_functions(3)


print(mul_2(13), mul_3(13))  # 13 to x dla lambdy
