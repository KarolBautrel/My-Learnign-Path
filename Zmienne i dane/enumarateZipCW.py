projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for p, l in zip(projects, leaders):
    print("The leader of ", p, " is ", l)

print()
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for p, d, l in zip(projects, dates, leaders):
    print("The leader of ", p, "started: ", d, " is ", l)

print()

for pos, (p, d, l) in enumerate(zip(projects, dates, leaders)):
    print(pos+1, "The leader of ", p, "started: ", d, " is ", l)
