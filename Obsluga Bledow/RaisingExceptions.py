
def proccess_Invoice(netto, brutto):
    if netto >= brutto:
        raise Exception("Netto should be equal or lower than Brutto")
    else:
        print("Processing invoice: netto = {}, brutto={}".format(netto, brutto))


def endOfMonth():
    netto = 1230
    brutto = 1000

    try:
        proccess_Invoice(netto, brutto)

    except ValueError as e:
        print("The values on invoice are incorrect: {}".format(e))
        # wskazanie ze blad moze pochodzic z bledu ktory teraz obslugujemy
        raise ValueError("Error when processing invoices ") from e
    except Exception as e:  # zglaszanie wczesniej stworzonego bledu : raise
        print("Error processing invoice : {}".format(e))


endOfMonth()
