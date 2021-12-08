days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

workdays = days.copy()

del workdays[-2:]
print(workdays, id(workdays))
print(days, id(days))
