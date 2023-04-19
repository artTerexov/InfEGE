with open("files/5232") as f:
    a = [[int(j) for j in i.split()] for i in f.readlines()]

a.sort()

resultRow = 0
currentRow = 0
resultPoints = 0
currentPoints = 0

for i in a:
    if currentRow == 0:
        currentRow = i[0]
    elif currentRow != i[0]:
        if currentPoints > resultPoints:
            resultRow = currentRow
            resultPoints = currentPoints
        currentRow = i[0]
        currentPoints = 0
    if i[1] % 2 != 0:
        currentPoints += 1

print(resultPoints, resultRow)
#
# buff = {}

# for i in a:
#     buff.setdefault(i[0], set())
#     if i[1] % 2 != 0:
#         buff[i[0]].add(i[1])
#
# for i in buff.keys():
#     buff[i] = len(buff.get(i))
#
# resultValue = max(buff.values())
#
# for i in buff.keys():
#     if buff.get(i) == resultValue:
#         print(resultValue,i)

