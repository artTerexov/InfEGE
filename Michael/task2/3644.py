# ¬w ∧ (y ∨ z → ¬x ∧ y)

print('x y z w F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not w) and ((y or z) <= ((not x) and y))
                if F == 1:
                    print(x, y, z, w, int(F))
