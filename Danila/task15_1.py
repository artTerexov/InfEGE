
# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))

for A in range(1, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (not(x <= 9) or ((x * x) <= A)) and (not((y * y) <= A) or (y <= 9))
            if F == 0:
                break
        if F == 0:
            break
    if F == 1:
        print(A)