instruction = ["say hello", 'say how are you',
               'ask for money', 'say thank you', 'say bye']
instructionApproved = []

for item in instruction:
    print("Adding instruction:", item)
    instructionApproved.append(item)
    if item == 'abort':
        print("Aborting")
        instructionApproved.clear()
        break
else:
    print("Following actions will be taken : ", instructionApproved)


# Loop while
print("-"*3)
i = 0  # zmienna sterujaca while
while i < len(instruction):
    print("Adding instruction:", instruction[i])
    instructionApproved.append(instruction[i])

    if instruction[i] == 'abort':
        print("Aborting")
        instructionApproved.clear()
        break

    i += 1

else:
    print("Following actions will be taken : ", instructionApproved)
