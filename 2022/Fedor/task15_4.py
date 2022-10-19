# ДЕЛ(x, A) → (¬ДЕЛ(x, 28) ∨ ДЕЛ(x, 42))

for A in range(1, 1000):
    for x in range(1, 1000):
        F = not(x % A == 0) or (not(x % 28 == 0) or (x % 42 == 0))
        if F == 0:
            break
    if F == 1:
        print(A)