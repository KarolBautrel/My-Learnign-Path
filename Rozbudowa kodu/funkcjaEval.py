var_x = 10
password = "My super secret password"

source = "password "
globals = globals().copy()  # kopiujemy globals do zmiennej globals, aby zmylic hakera
del globals['password']  # usuwamy wartosc "password" z globals
# Eval wykona kawalek programu zapisany w source
result = eval(source, globals)  # eval da blad poniewaz nie znajdzie "password"
print(result)

# print(globals())

# EVAL MOZE TYLKO WYKONAC WYRAZENIA (CZYLI COS CO MOZE BYC PRZYPISANE DO ZMIENNEJ)
