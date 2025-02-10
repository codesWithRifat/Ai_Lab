""" Given a list of numbers, remove
    duplicates and sort in ascending order."""
numList = [4, 3, 7, 4, 9, 2, 7, 1]
numList.sort()
i = 0
while i < len(numList) - 1:
    if numList[i] == numList[i + 1]:
        numList.remove(numList[i])
    else:
        i += 1

print(numList)

