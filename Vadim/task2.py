# ((y → x) ∨ (¬z ∧ w)) ≡ (w ≡ x).
# y -> x = not y or x
print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = ((not y or x) or (not z and w)) == (w == x)
                if F == 1:
                    print(x, y, z, w, F)
