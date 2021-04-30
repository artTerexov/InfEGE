def T(n):
    if n == 19:
        return 1
    if n > 19:
        return 0
    return T(n + 1) + T(n + 3) + T(n * n)


print(T(2))
