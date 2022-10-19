# ((x → y) ∧ (y → w)) ∨ (z ≡ (x ∨ y)).

print('x y z w F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((x <= y) and (y <= w)) or (z == (x or y))
                if F == 0:
                    print(x, y, z, w, int(F))

# Проверка
x, y, z, w = 1, 0, 0, 1
F = ((x <= y) and (y <= w)) or (z == (x or y))
print(F)