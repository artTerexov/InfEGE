# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)
# https://inf-ege.sdamgia.ru/problem?id=9804

for A in range(0, 1000):
    for x in range(0, 1000):
        F = (x & 29 == 0) or (x & 17 != 0 or x & A != 0)
        if F == 0:
            break
    if F == 1:
        print(A)