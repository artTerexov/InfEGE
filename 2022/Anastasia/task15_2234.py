#2234
#(A < 50) ∧ (¬ДЕЛ(x, A) → (ДЕЛ(x, 10) → ¬ДЕЛ(x, 12)))

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((A < 50) and ((x % A == 0) or (not (x % 10 == 0)) or not(x % 12 == 0))) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)

