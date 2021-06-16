def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n/2)
    if n % 2 != 0:
        return 1 + F(n-1)


b = []
for n in range(1, 501):
    if F(n) == 3:
        b.append(n)
print(len(b))