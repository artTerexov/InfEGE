def F(n):
    if n >= 300:
        return n
    if n < 10000 and n % 6 == 0:
        return n // 6 + F(n // 6 + 2)
    return n + F(n + 2)


print(F(264) - F(7))


