# https://inf-ege.sdamgia.ru/problem?id=27422

for i in range(174457, 174505):
    numDel = []
    for j in range(2, i // 2):
        if i % j == 0:
            numDel.append(j)
            if len(numDel) == 3:
                break
    if len(numDel) == 2:
        print(numDel[0], numDel[1], numDel[0] * numDel[1])