# F = ¬(y→ (x≡w))/\(z→x)
# ¬ ---> not
# → ---> A -> B => not A \/ B
print("x y z w F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = not(not y or (x == w)) and (not z or x)
                if F == 1:
                    print(x, y, z, w, int(F))

