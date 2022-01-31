def F(n):
    if n == 0:
        return 3
    if (0 < n < 15) or (0 < n == 15):
        return F(n - 1)
    if 15 < n < 100:
        return 2.5 * F(n - 3)
    if n > 100 or n == 100:
        return 3.3 * F(n - 2)


print(F(100))
