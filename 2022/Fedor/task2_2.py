# Логическая функция F задаётся выражением ((¬y → w) → (x → z)) → (x → w).
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = not(not(y or w) or (not x or z)) or (not x or w)
                if F == 0:
                    print(x, y, z, w)