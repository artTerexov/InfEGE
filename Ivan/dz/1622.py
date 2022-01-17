# Логическая функция F задаётся выражением (z ∨ y) → (x ≡ z).
#
print("X Y Z F")
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = ((z or y) <= (x == z))
            if int(f) == 0:
                print(int(x), int(y), int(z), int(f))
            