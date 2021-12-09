# obiekt jest iterable
aTuple = (1, 2, 3, 4, 5)

# przypisanie iteratora obiektowi aTuple
iTuple = iter(aTuple)
print(next(iTuple))

# obiekt jest iterable, ale nie ma iteratora
aList = [1, 2, 3, 4, 5]

# przypisanie iteratora
iList = iter(aList)

print(next(iList))


aSet = {1, 2, 3, 4, 5}

iSet = iter(aSet)

print(next(iSet))
print(next(iSet))

print(next(iSet))
