import functools
import time


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        delta_time = time_stop - time_start
        print("Funkcja o nazwie{} wykonana w czasie{}".format(
            a_function, delta_time))
        return v
    return a_wrapped_function


@ wrapper_time
def get_sequence(n):

    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v


#wrapper_get_sequence = wrapper_time(get_sequence)

print(get_sequence(1))
