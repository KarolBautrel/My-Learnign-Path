workDays = [19, 21, 22, 21, 20, 22]

print(workDays)


# enumerate pozwala nam ponumerowac liste w sposob (0,wartosc indeksu), (1, wartosc indeksu)
enumerateDays = list(enumerate(workDays))
print(enumerateDays)

for pos, value in enumerateDays:
    print("Position: ", pos, "Value: ", value)

months = ["I", "II", "III", "IV", "V", "VI"]

for days, month in zip(workDays, months):
    print(month, ':', days)

for pos, (m, d) in enumerate(zip(months, workDays)):
    print(str(pos)+".", m, d)
