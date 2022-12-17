# (x ∈ P) → ( ((x ∈ Q) ∧ ¬(x ∈ A)) → ¬(x ∈ P)) )

a = []
for a1 in range(100, 200):
    for a2 in range(a1, 201):
        flag = True
        for x in range(1, 500):
            if ((117 <= x <= 158) <= (((129 <= x <= 180) and not(a1 <= x <= a2)) <= (not(117 <= x <= 158)))) == 0:
                flag = False
                break
        if flag:
            a.append(a2 - a1)

print(min(a))