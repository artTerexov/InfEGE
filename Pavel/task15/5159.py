# (ДЕЛ(x, 6) → ¬ДЕЛ(x, 14)) ∨ (x + A ≥ 70) ∧ ДЕЛ(A, 20)

for A in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        if (((not(x % 6 == 0)) or (not(x % 14 == 0))) or (x + A >= 70) and (A % 20 == 0)) == 0:
            flag = 0
            break
    if flag == 1:
        print(A)