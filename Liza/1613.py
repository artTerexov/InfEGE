# 1613

print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = x and (y and z or z and w or y and (not w))
                if F:
                    print(x, y, z, w)