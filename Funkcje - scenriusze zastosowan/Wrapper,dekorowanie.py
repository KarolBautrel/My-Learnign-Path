# wrapper pozwala obudowac fukcje w funkcje dodatkowa, ktora zrobi cos jeszcze
import datetime
import functools  # biblioteka do modyfikacji funkcji/ dekorator


def CreateFunctionWithWrapper(func):
    # to jest funkcja wykonujaca funkcje ktora podana jest w argumencie Wrapper i nie tylko
    def func_with_wrapper(*args, **kwargs):
        print("Function started at {}".format(func.__name__,
                                              datetime.datetime.now().isoformat()))  # podaje kiedy uruchomiona zostala funkcja
        print("Following argument were used: ", args, kwargs)
        # wykonuje funkcje z argumentu wczesniejszej (*args,**kwargs to argumenty ktore bedziemy podawac do zmiennej)
        result = func(*args, **kwargs)  # Wykonuje funkcje (print xxxxx)
        print("Function returned {}".format(result))
        return result  # wyswietla co funkcja zwraca
    return func_with_wrapper


# biblioteka functools pozwala korzystac z malpki, oznaczamy dzieki temu, ze ta funkcja bedzie zawsze uzywana
@CreateFunctionWithWrapper  # dekorator
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print("Changing salary for {} to {} as bonus = {}".format(
        emp_name, new_salary, is_bonus))
    return new_salary


print(ChangeSalary('Johnson', 2000, True))
