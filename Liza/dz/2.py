# (a ∧ b) ∨ (a ∧ ¬c)
print('a b c')
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            F = (a and b) or (a and (not c))
            if F:
                print(a, b, c)