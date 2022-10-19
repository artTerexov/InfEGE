# https://inf-ege.sdamgia.ru/problem?id=27858

maximum = 0
kolvo = 0
for i in range(120115, 120201):
    b = [1, i]
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            b.append(j)
    if len(b) > kolvo:
        kolvo = len(b)
        maximum = i

print(kolvo, maximum)