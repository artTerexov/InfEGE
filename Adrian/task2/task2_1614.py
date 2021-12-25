# x ∧ (z ∧ ¬w ∨ y ∧ ¬w ∨ y ∧ ¬z)

print("x y z w F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = x and (z and (not w) or y and (not w) or y and (not z))
                if F == 1:
                    print(x, y, z, w, F)

