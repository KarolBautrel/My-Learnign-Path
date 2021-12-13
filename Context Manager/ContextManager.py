import time


class Time_measure:

    def __init__(self):
        pass
    # aby contextManager w klasie dzialał, nalezy uzyc metody __enter__

    def __enter__(self):
        print("entering")
        self.__start = time.time()  # tutaj zapisywany bedzie czas podczas startu
        return self

    def __exit__(self, exc_type, exc_value, trace):
        print("Exiting")
        self.__stop = time.time()  # pobranie czasu
        self.difference = self.__stop - self.__start  # roznica czasu miedzy start a stop
        print("Execution time: {}". format(self.difference))


with Time_measure():
    time.sleep(3)
