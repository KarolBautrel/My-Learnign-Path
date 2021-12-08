clients = {
    "INFO": 0.5,
    "DATA": 0.2,
    "SOFT": 0.2,
    "INTER": 0.1,
    "OMEGA": 0.0
}

myClient = input("Enter client name: ")
totalCost = 7200
try:
    ratio = float(input("Enter new ratio: "))
    print("The default '%' ratio for {} is {}, the new is {} ".format(
        myClient, clients[myClient], ratio))
    print("The cos for {} is {}".format(myClient, ratio * totalCost))
    print("The new ratio in comparison to old is {}".format(
        clients[myClient]/ratio))
except KeyError as e:  # KeyError dotyczy blednego wprowadzenia uzytkownika
    print("Client {} dont exist".format(e))
# ValueError dotyczy bledu do wartosci, ktorej nie mozna skonwertowac (np dodanie inta i str)
except ValueError as e:
    print("The value {} is not correct value".format(e))
except ZeroDivisionError as e:  # Wywola sie klasa Exception, ktorej instancja jest e i w niej mozemy pdoac sczegoly bledu
    print("Division by zero is not allowed\n", "Details {}".format(e))
