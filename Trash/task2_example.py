# (¬x ∧ y ∧ z) ∨ (¬x ∧ ¬y ∧ z) ∨ (¬x ∧ ¬y ∧ ¬z).
# https://inf-ege.sdamgia.ru/problem?id=9752

print("x y z F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            F = (not x and y and z) or (not x and not y and z) or (not x and not y and not z)
            if F == 1:
                print(x, y, z, F)