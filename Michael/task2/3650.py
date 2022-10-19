# a ≡ b ∨ c ≡ b

print('a b c F')

for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            F = (a == (b or c)) == b
            if F == 1:
                print(a, b, c, int(F))
