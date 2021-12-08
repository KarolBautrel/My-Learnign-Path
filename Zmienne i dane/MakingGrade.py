def student_ranking(student_scores, student_names):
    newList = []
    enumeratedList = []
    for scores, names in zip(student_scores, student_names):
        new = names + ": " + str(scores)
        newList.append(new)

    for pos, elem in enumerate(newList):
        new2 = str(pos)+'.', elem
        enumeratedList.append(new2)

    print(enumeratedList)


student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names = ['Joci', 'Sara', 'Kora', 'Jan', 'John', 'Bern', 'Fred']
print(student_ranking(student_scores, student_names))
