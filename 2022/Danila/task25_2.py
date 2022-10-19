# https://inf-ege.sdamgia.ru/problem?id=27422

for i in range(174457, 174506):
    b = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            b.append(j)
        if len(b) > 2:
            break
    if len(b) == 2:
        print(*b)


