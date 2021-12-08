for i in range(10, 1, -1):
    print(i)

list = list((range(10)))
print(list, type(list), id(list))
list2 = list.copy()

print(id(list2))


print(list[-1::-1])


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

my_days = days[:]
my_days = my_days + ['Saturday', 'Sunday']

print(days[-2:])
