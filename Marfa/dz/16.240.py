def f(n):
    if n < 6:
        return n + f(n+3) * f(2*n)
    else:
        return 2 * n


print(f(3))