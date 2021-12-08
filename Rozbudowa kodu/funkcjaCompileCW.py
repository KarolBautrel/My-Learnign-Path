import time
import math


formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []
for i in range(1000000):
    argument_list.append(i/10)
for formulas in formulas_list:
    result_list = []
    print(formulas_list[0])
    start = time.time()
    firstFormula = compile(formulas, formulas, 'eval')
    for x in argument_list:
        result_list.append((eval(firstFormula)))
    stop = time.time()

    print(result_list)
    deltaTime = stop - start
print("Calculation Type : ", deltaTime)
