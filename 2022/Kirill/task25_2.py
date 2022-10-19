L = []
for i in range(190201, 190261):
    if len(L) == 4:
        print(*L[3:1:-1])
    L.clear()
    for j in range(1, i + 1):
        if i % j == 0 and j % 2 == 0:
            L.append(j)
