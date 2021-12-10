import random


def generator_with_sum(numberOfValues, asserted_sum):

    trial = 0
    numbers = list(range(numberOfValues))

    while True:
        trial += 1
        for i in range(numberOfValues):
            numbers[i] = random.randint(1, 100)

        if sum(numbers) == asserted_sum:
            krotka = (trial, numbers)
            yield krotka
            trial = 0


for i in range(10):
    (number_of_trials, numbers) = next(generator_with_sum(3, 100))
    print(number_of_trials, numbers)
