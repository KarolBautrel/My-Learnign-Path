optionList = ['load data', 'export data', 'analyze&predict']
choice = "x"


def display_options(s):
    return str(s)


while choice:
    choice = display_options(3)
    if choice:
        try:
            choice_num = int(choice)
            if choice_num < 3:
                print("Number is: ", choice_num, "its is",
                      optionList[int(choice_num)])
                break
            else:
                print("Number is out of range:")
                break
        except:
            print("Cant make integer")
            break
    else:
        print("End of")
        break
