def T(n, f):
    if n == 20 and f != 0:
        return 1
    if n == 20 and f == 0:
        return 0
    if n > 20:
        return 0
    if n == 10:
        f += 1
    return T(n + 1, f) + T(n * 2, f)


print(T(1, 0))
