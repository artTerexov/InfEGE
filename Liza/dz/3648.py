# (a → d) ∧ ¬(b → c)
print('a', 'b', 'c', 'd')
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                F = (a <= d) and (not(b <= c))
                if F:
                    print(a, b, c, d)
