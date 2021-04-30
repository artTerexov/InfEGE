# ((x < A) → (x2 < 81)) ∧ ((y2 ≤ 36) → (y ≤ A))

count = 0

for A in range(-1000, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            F = (x >= A or x * x < 81) and (y * y > 36 or y <= A)
            if F == 0:
                break
        if F == 0:
            break
    if F == 1:
        count += 1

print(count)