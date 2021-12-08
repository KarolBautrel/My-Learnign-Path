import datetime
import functools
import os


def wrapper_with_log_file(logged_action, logFilePath):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            file = open(logFilePath, "a")
            file.write('-'*50+"\n")
            file.write("The action has been taken: {} on{}\n".format(
                logged_action, path))
            file.write("The action started at {}\n".format(
                datetime.datetime.now()))
            result = func(path)
            file.close()
            return result
        return the_real_wrapper
    return wrapper_with_log_to_known_file


@wrapper_with_log_file("FILE CREATE", "create.txt")
def create_file(path):
    print('creating file {}'.format(path))
    open(path, "w+")


@wrapper_with_log_file("FILE DELETE", "delete.txt")
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)


print(create_file("create.txt"))
