print("x y z w F")
for x in (False, True):
    for y in (False, True):
        for z in (False, True):
            for w in (False, True):
                f = (x == (not z)) or ((x or w) == y)
                if int(f) == 0:
                    print(int(x), int(y), int(z), int(w), int(f))
