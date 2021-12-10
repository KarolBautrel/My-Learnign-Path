# file = open(
# E:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Generatory\data.txt")
with open("E:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Generatory\data.txt") as file:
    records = []
    for line in file:
        if line.startswith("ACTION") and ":" in line:
            # split(':',1) => rozbijanie ze wzgledu na jaki znak i ile razy w linijce
            # rozbicie linijki ze wzgledu na znak dwukropka
            type, action = line.rstrip("\n").split(':', 1)
            record = (type, action)
            records.append(record)

print(records)
print(records[2][1])


# GENERATOR
def get_records(file):
    with open(file) as f:
        for line in f:
            if line.startswith("ACTION") and ':' in line:
                type, action = line.rstrip('\n').split(':', 1)
                record = (type, action)
                yield record


path = "E:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Generatory\data.txt"
for i in get_records(path):
    print("The type is {} and the action is {}". format(record[0], record[1]))
