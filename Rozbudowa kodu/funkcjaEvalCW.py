import math

argument_list = []

for x in range(100):
    n = (x*0.01)
    argument_list.append(n)


formula = input("Write the equation: (argument x)")

for x in argument_list:
    print(x, eval(formula))
