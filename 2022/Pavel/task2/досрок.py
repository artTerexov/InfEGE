# отрицание -> not
# коньюнкция -> and
# дизьюнкция -> or
# импликация -> (A -> B = not A or B)
# эквиваленция -> ==

print('x y z w F')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (not(not x or z)) or (y == w) or (not y)
                if F == 0:
                    print(x, y, z, w, int(F))
