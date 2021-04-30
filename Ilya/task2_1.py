print("x y z w")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (y <= x) or not((x <= z) and (z <= x)) and not w
                if F == 0:
                    print(x, y, z, w)