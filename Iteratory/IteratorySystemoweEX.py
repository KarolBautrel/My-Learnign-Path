import csv

with open('E:\Coding\Python\Python\Kody nauka\Python dla srednio zaawansowanych\Iteratory\iterations.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    # print('|'.join(row))
    while True:
        try:
            data = next(csvreader)
            print(data)
        except StopIteration:
            break
