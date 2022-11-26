# (ДЕЛ(x, 2) → ¬ДЕЛ(x, 3)) ∨ (x + A ≥ 80)

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)) == 0:
            flag = False
            break
    if flag:
        print(A)
        break