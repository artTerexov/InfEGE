# (w → y) ∧ ((x → z) ≡ (y → x))
# ∧ -> and
# w → y -> not w or y
# → -> <=
# ≡ -> ==

print("x y z w")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not w or y) and ((not x or z) == (not y or x))
                if F == 1:
                    print(x, y, z, w)