# (x + y ≤ 22) ∨ (y ≤ x – 6) ∨ (y ≥ A)


for A in range(0, 100):
    flag = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x + y <= 22) or (y <= x - 6) or (y >= A)) == 0:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(A)

