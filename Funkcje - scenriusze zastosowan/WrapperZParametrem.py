import datetime
import functools  # biblioteka do modyfikacji funkcji/ dekorator


# przyjecie sciezki pliku
def CreateFunctionWithWrapper_LogToFile(logFilePath):
    # wrapper bedzie pisal do wlasciwego pliku dzieki funkcji powyzej
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, "a")  # otworz plik
            file.write('-'*50)
            file.write("\n")
            file.write("Function started at {}\n".format(
                datetime.datetime.now()))  # zapisz w pliku
            file.write("Following argument were used:\n")
            # parametry arg(tuplety) musialy zostac zmienione w string
            # zamiast format mozna bylo str(x)
            file.write(' '.join("{}".format(x) for x in args))
            file.write("\n")
            # parametry kwarg musialy zostac zmienione w string
            file.write(" ".join("{}={}" for (k, v) in kwargs.items()))
            result = func(*args, **kwargs)
            file.write("Function returned {}\n".format(result))
            file.close()
            return result  # wyswietla co funkcja zwraca
        return func_with_wrapper
    return CreateFunctionWithWrapper


# biblioteka functools pozwala korzystac z malpki, oznaczamy dzieki temu, ze ta funkcja bedzie zawsze uzywana
# dekorator(okreslenie jaki plik w nawiasie)
@CreateFunctionWithWrapper_LogToFile("log_it.txt")
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print("Changing salary for {} to {} as bonus = {}".format(
        emp_name, new_salary, is_bonus))
    return new_salary


# okreslenie jaki plik
@CreateFunctionWithWrapper_LogToFile("change_position.txt")
def ChangePosition(emp_name, new_position):
    print('Changing postion for{} to {}'.format(emp_name, new_position))
    return new_position


print(ChangeSalary('Johnson', 2000, True))
print(ChangePosition("Michael", "Salesman"))
