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
    print("The '%' ratio for {} is {} ".format(myClient, clients[myClient]))
except Exception as e:  # Wywola sie klasa Exception, ktorej instancja jest e i w niej mozemy pdoac sczegoly bledu
    print("Sorry we have an error\n", "Details {}".format(e))
else:  # jesli w linijce 12 nie bedzie bledu to wykona sie tez to
    print("The cos for {} is {} ".format(
        myClient, clients[myClient]*totalCost))
finally:
    print("--Calculation Completed--")
