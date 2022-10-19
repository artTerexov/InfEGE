print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not y or x) or not((not x or z) and (not z or x)) and not w
                if F == 0:
                    print(x, y, z, w)
