optionList = ['load data', 'export data', 'analyze&predict']
choice = -1

print("0.Load data")
print("1.Export data")
print("2. analyze & predict")

choice = input("Pick your option: ")
if choice.isnumeric():
    pass
    if int(choice) < 3:
        print("Number is: ", choice, "its is", optionList[int(choice)])
    else:
        print("Out of range")
else:
    print("This is not a number")
