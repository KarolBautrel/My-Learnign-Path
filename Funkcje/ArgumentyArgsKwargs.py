# *args tworzy w tuplet a **kwargs w dictionary
# args odpowiada za wiele argumentow, **kwargs za dodatkowe argumenty z wartoscia
def BuyMe(prefix="Please buy me", what="something nice", *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)


products = ['milk', 'break', 'flakes']
parameters = {'price': 'low', 'time': 'now'}

# gwiazdki oznaczaja ze odnosimy sie do arg i kwargs
print(BuyMe("Buy me", "newspaper", *products, **parameters))
